#!/usr/bin/env bash
set -euo pipefail

# Work from the script's directory
cd "$(dirname "$0")"

REQUIRED_VERSION="3.14.10"
PYTHON="python"

# Check uv is installed
if ! command -v uv >/dev/null 2>&1; then
    echo "uv is not installed. Run: pip install uv"
    exit 1
fi

# Check existing Python version
NEEDS_VENV=true

if [ -x "$PYTHON" ]; then
    CURRENT_VERSION=$("$PYTHON" -c \
        'import platform; print(platform.python_version())')

    if [ "$CURRENT_VERSION" = "$REQUIRED_VERSION" ]; then
        NEEDS_VENV=false
        echo "Python $REQUIRED_VERSION is already installed."
    fi
fi

# Install Python and create/recreate virtual environment
if [ "$NEEDS_VENV" = true ]; then
    echo "Setting up Python $REQUIRED_VERSION..."

    uv python install "$REQUIRED_VERSION"
    uv venv --seed --python "$REQUIRED_VERSION" --clear .venv
fi

# Upgrade pip
"$PYTHON" -m pip install --upgrade pip

# Install requirements
if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    "$PYTHON" -m pip install -r requirements.txt
fi

# Find and upgrade outdated packages
echo "Checking for outdated packages..."

"$PYTHON" -m pip list --outdated --format=json |
    "$PYTHON" -c '
import json
import subprocess
import sys

packages = json.load(sys.stdin)

for package in packages:
    name = package["name"]
    print(f"Updating {name}...", flush=True)

    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", name],
        check=True
    )
'

# Export updated requirements
"$PYTHON" -m pip freeze > requirements.txt

echo ""
echo "Setup complete!"
"$PYTHON" --version
