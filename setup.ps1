# Define source and destination paths
$sourcePath = Join-Path -Path (Get-Location).Path -ChildPath "osint_recon.py"
$desktopPath = [Environment]::GetFolderPath("Desktop")
$destinationPath = Join-Path -Path $desktopPath -ChildPath "osint_recon.py"

# Verify the source file exists
if (-Not (Test-Path -Path $sourcePath)) {
    Write-Host "[ERROR] Cannot find osint_recon.py in the current directory: $sourcePath"
    Write-Host "[INFO] Please ensure osint_recon.py is in the same folder as setup.ps1."
    exit 1
}

# Copy the script to the user's desktop
Write-Host "[INFO] Copying osint_recon.py to Desktop..."
Copy-Item -Path $sourcePath -Destination $destinationPath -Force

# Confirm the setup is complete
Write-Host "[SUCCESS] osint_recon.py has been placed on your Desktop."
Write-Host "Run the script from the Desktop using: python osint_recon.py"
