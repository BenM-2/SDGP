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

$needsVenv = $true
if (Test-Path $Python) {
    $currentVersion = & $Python -c "import platform; print(platform.python_version())"
    if ($LASTEXITCODE -eq 0 -and $currentVersion -eq $RequiredVersion) {
        $needsVenv = $false
        Write-Host "Python $RequiredVersion venv already exists."
    }
}

if ($needsVenv) {
    uv python install $RequiredVersion
    Assert-Success

    uv venv --seed --python $RequiredVersion --clear $VenvDir
    Assert-Success
}

& $Python -m pip install --upgrade pip
Assert-Success

if (Test-Path "requirements.txt") {
    & $Python -m pip install -r requirements.txt
    Assert-Success
}

Write-Host "Setup complete!"
& $Python --version