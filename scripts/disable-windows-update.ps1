#   Disables Windows Update Service


$services = @(
    "wuauserv" # Windows Update

)

foreach ($service in $services) {
    Write-Output "Disabling Windows Update"
    Get-Service -Name $service | Set-Service -StartupType Disabled
}
Write-Output "Disabled Windows Update"