import subprocess, sys, os, shutil

print("Make Sure This is Running As Admin!")
print("What would you like to do?")
print("[B] - Block Telemetry")
print("[C] - Compatibility Check")
print("[D] - Full Debloat")
print("Type ""help (letter)"" to see what a command does")
choice = input("> ")

if choice == "B":
	p = subprocess.Popen(["powershell.exe",
		"scripts\\block-telemetry.ps1"],
		stdout=sys.stdout)
	p.communicate()

if choice == "C":
	p = subprocess.Popen(["powershell.exe",
              "scripts\\compatchk.ps1"], 
              stdout=sys.stdout)
	p.communicate()

if choice == "O":
	p = subprocess.Popen(["powershell.exe",
              "scripts\\remove-onedrive.ps1"], 
              stdout=sys.stdout)
	p.communicate()



