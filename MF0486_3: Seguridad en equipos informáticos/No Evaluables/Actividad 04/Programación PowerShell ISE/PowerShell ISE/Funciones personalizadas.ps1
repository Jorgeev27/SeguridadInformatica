function Get-DiskSpace {
 param (
 [string]$drive = "C"
 )
 Get-PSDrive -Name $drive | Select-Object Name,
@{Name="FreeSpace(GB)";Expression={ "{0:N2}" -f ($_.Free/1GB) }}
}
# Usar la función
Get-DiskSpace -drive "C"