# Sets up Powershell to run scripts from third parties

#Requires -RunAsAdministrator
Set-ExecutionPolicy Unrestricted
ls -Recurse *.ps1 | Unblock-File
ls -Recurse *.psm1 | Unblock-File
"You are ready to debloat Windows 10"
