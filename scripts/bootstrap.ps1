Param(
    [string]$VenvPath = ".venv",
    [string]$Requirements = "requirements.txt"
)

Write-Host "Checking for Python..."
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Error "Python not found in PATH. Install Python 3.8+ and try again."
    exit 1
}

Write-Host "Creating virtual environment at $VenvPath..."
python -m venv $VenvPath

$activate = Join-Path $VenvPath "Scripts\Activate.ps1"
if (-not (Test-Path $activate)) {
    Write-Error "Activation script not found at $activate"
    exit 1
}

Write-Host "Upgrading pip and installing requirements..."
& "$VenvPath\Scripts\python.exe" -m pip install --upgrade pip
if (Test-Path $Requirements) {
    & "$VenvPath\Scripts\python.exe" -m pip install -r $Requirements
} else {
    Write-Host "No $Requirements found; skipping install."
}

Write-Host "Done. To activate run: .\$VenvPath\Scripts\Activate.ps1"
