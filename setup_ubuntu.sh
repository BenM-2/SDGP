#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

REQUIRED_VERSION="3.14.10"
VENV_DIR=".venv"
PYTHON="$VENV_DIR/bin/python"

export PATH="$HOME/.local/bin:$PATH"

if ! command -v uv >/dev/null 2>&1; then
    echo "uv is not installed. Run: sudo apt install pipx && pipx install uv"
    exit 1
fi

uv python install "$REQUIRED_VERSION"
uv sync --python "$REQUIRED_VERSION"

echo "Setup complete!"
"$PYTHON" --version