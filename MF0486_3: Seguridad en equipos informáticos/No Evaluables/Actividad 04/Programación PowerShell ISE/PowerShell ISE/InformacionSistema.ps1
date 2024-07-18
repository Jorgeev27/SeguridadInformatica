$os = Get-ComputerInfo | Select-Object CsName, WindowsVersion, OsArchitecture;
Write-Host "Nombre del Ordenador: $($os.Csname)";
Write-Host "Version de Windows: $($os.WindowsVersion)";
Write-Host "OS Architecture: $($os.OsArchitecture)";