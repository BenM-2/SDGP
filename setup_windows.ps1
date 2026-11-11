$ErrorActionPreference = "Stop"

# Work from the script's directory
Set-Location $PSScriptRoot

$RequiredVersion = "3.14.10"
$VenvDir = ".venv"
$Python = Join-Path $PSScriptRoot "$VenvDir\Scripts\python.exe"

# uv's standalone installer puts it in ~/.local/bin; make sure it's found
$env:PATH = "$HOME\.local\bin;$env:PATH"

function Assert-Success {
    if ($LASTEXITCODE -ne 0) { exit 1 }
}

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    [Console]::Error.WriteLine("uv is not installed. Run: winget install --id=astral-sh.uv -e")
    [Console]::Error.WriteLine("Then restart your terminal and re-run this script.")
    exit 1
}

uv python install $RequiredVersion
Assert-Success

uv sync --python $RequiredVersion
Assert-Success

Write-Host "Setup complete!"
& $Python --version