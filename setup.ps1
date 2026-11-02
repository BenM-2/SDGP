$ErrorActionPreference = "Stop"

# Work from the script's directory
Set-Location $PSScriptRoot

$requiredVersion = "3.14.10"
$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

# Check uv is installed
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Error "uv is not installed. Run: pip install uv"
    exit 1
}

# Check if the virtual environment uses the correct Python
$needsVenv = $true

if (Test-Path $python) {
    $currentVersion = & $python -c "import platform; print(platform.python_version())"

    if ($currentVersion -eq $requiredVersion) {
        $needsVenv = $false
        Write-Host "Python $requiredVersion is already installed."
    }
}

# Install Python and create/recreate virtual environment
if ($needsVenv) {
    Write-Host "Setting up Python $requiredVersion..."

    uv python install $requiredVersion
    if ($LASTEXITCODE -ne 0) { exit 1 }

    uv venv --seed --python $requiredVersion --clear .venv
    if ($LASTEXITCODE -ne 0) { exit 1 }
}

# Upgrade pip
& $python -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { exit 1 }

# Install packages from requirements.txt
if (Test-Path "requirements.txt") {
    Write-Host "Installing requirements..."
    & $python -m pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) { exit 1 }
}

# Find outdated packages
Write-Host "Checking for outdated packages..."

$outdatedJson = & $python -m pip list --outdated --format=json
if ($LASTEXITCODE -ne 0) { exit 1 }

$outdated = @($outdatedJson | ConvertFrom-Json)

foreach ($package in $outdated) {
    Write-Host "Updating $($package.name)..."

    & $python -m pip install --upgrade $package.name

    if ($LASTEXITCODE -ne 0) {
        Write-Warning "Failed to update $($package.name)"
        exit 1
    }
}

# Save updated requirements
& $python -m pip freeze | Set-Content requirements.txt

Write-Host ""
Write-Host "Setup complete!"
& $python --version
