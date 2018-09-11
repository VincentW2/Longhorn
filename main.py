import subprocess
import sys
import os
import shutil

print("Make Sure This is Running As Admin!")
print("What would you like to do?")
print("[A] - Ultra Debloat")
print("[C] - Compatibility Check")
choice = input("> ")

if choice == "C":
	p = subprocess.Popen(["powershell.exe",
              "scripts\\compatchk.ps1"], 
              stdout=sys.stdout)
	p.communicate()