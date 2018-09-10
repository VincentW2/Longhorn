import subprocess
import sys
import os
import shutil

print("Make Sure This is Running As Admin!")
print("What would you like to do?")
print("[A] - Ultra Debloat")
print("[C] - Compat Check")
choice = input("> ")

if choice == "C":
	p = subprocess.Popen(["powershell.exe", 
              "./adminchk.ps1"], 
              stdout=sys.stdout)
	p.communicate()