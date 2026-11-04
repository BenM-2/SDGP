#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

REQUIRED_VERSION="3.14.10"
VENV_DIR=".venv"
PYTHON="$VENV_DIR/bin/python"

export PATH="$HOME/.local/bin:$PATH"

if ! command -v uv >/dev/null 2>&1; then
    echo "uv is not installed. Run: brew install pipx && pipx install uv"
    exit 1
fi

NEEDS_VENV=true
if [ -x "$PYTHON" ] && [ "$("$PYTHON" -c 'import platform; print(platform.python_version())')" = "$REQUIRED_VERSION" ]; then
    NEEDS_VENV=false
    echo "Python $REQUIRED_VERSION venv already exists."
fi

if [ "$NEEDS_VENV" = true ]; then
    uv python install "$REQUIRED_VERSION"
    uv venv --seed --python "$REQUIRED_VERSION" --clear "$VENV_DIR"
fi

"$PYTHON" -m pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    "$PYTHON" -m pip install -r requirements.txt
fi

echo "Setup complete!"
"$PYTHON" --version
