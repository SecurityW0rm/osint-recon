# Define source and destination paths
$sourcePath = ".\OSINT"
$desktopPath = [Environment]::GetFolderPath("Desktop")
$destinationPath = Join-Path -Path $desktopPath -ChildPath "osint_recon.py"

# Copy the script to the user's desktop
Write-Host "[INFO] Copying osint_recon.py to Desktop..."
Copy-Item -Path $sourcePath -Destination $destinationPath -Force

# Confirm the setup is complete
Write-Host "[SUCCESS] osint_recon.py has been placed on your Desktop."
Write-Host "Run the script from the Desktop using: python osint_recon.py"
