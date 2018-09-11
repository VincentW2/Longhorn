import subprocess
import sys
import os
import shutil

print("Make Sure This is Running As Admin!")
print("What would you like to do?")
print("[B] - Block Telemetry")
print("[C] - Compatibility Check")
print("[D] - Full Debloat")
print("Type ""help (letter)"" to see what a command does")
choice = input("> ")


if choice == "C":
	p = subprocess.Popen(["powershell.exe",
              "scripts\\compatchk.ps1"], 
              stdout=sys.stdout)
	p.communicate()

if choice == "D":
	p = subprocess.Popen(["powershell.exe",
		"scripts\\block-teleetry.ps1"],
		stdout=sys.stdout)
	p.communicate()

	