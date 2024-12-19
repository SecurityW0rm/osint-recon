# Get the current script directory
$scriptDir = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent

# Define the destination (user's Desktop)
$desktopPath = [Environment]::GetFolderPath('Desktop')

# Check if PySIEM.py exists in the current directory
if (Test-Path "$scriptDir\OSINT.py") {
    # Copy the script to the Desktop
    Copy-Item -Path "$scriptDir\OSINT.py" -Destination "$desktopPath\OSINT.py" -Force

    # Confirm the script has been moved
    Write-Host "OSINT.py has been moved to your Desktop successfully."
    Write-Host "You can now run the script from your Desktop by navigating there in PowerShell."
    Write-Host "Example: cd $desktopPath && python .\OSINT.py"
} else {
    Write-Host "Error: OSINT.py not found in the current directory." -ForegroundColor Red
    Write-Host "Please ensure you're running this script from the cloned repository folder." -ForegroundColor Red
}
