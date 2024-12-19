# Locate the file starting with "OSINT"
$sourcePath = Get-ChildItem -Path (Get-Location).Path -Filter "OSINT*" | Select-Object -First 1 | ForEach-Object { $_.FullName }
$desktopPath = [Environment]::GetFolderPath("Desktop")
$destinationPath = Join-Path -Path $desktopPath -ChildPath "osint_recon.py"

# Verify the source file exists
if (-Not $sourcePath) {
    Write-Host "[ERROR] Cannot find a file starting with 'OSINT' in the current directory: $(Get-Location)"
    Write-Host "[INFO] Please ensure the file named 'OSINT' is in the same folder as setup.ps1."
    exit 1
}

# Rename and copy the script to the user's desktop
Write-Host "[INFO] Copying and renaming the file to 'osint_recon.py' on Desktop..."
Copy-Item -Path $sourcePath -Destination $destinationPath -Force

# Confirm the setup is complete
Write-Host "[SUCCESS] The file has been renamed to 'osint_recon.py' and placed on your Desktop."
Write-Host "Run the script from the Desktop using: python osint_recon.py"
