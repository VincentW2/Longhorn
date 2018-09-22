def longhorn():

	import subprocess, sys, os, shutil

	print("MAKE SURE THIS IS RUNNING AS ADMIN")
	print("[B] - Block Telemetry")
	print("[O] - Remove Onedrive")
	print("[S] - Setup Longhorn")
	print("[X] - Exit")
	while True:
		choice = input("> ")

		if choice == "B":
			p = subprocess.Popen(["powershell.exe",
				"scripts\\block-telemetry.ps1"],
				stdout=sys.stdout)
			p.communicate()

		if choice == "O": 
			p = subprocess.Popen(["powershell.exe",
	            "scripts\\remove-onedrive.ps1"], 
	            stdout=sys.stdout)
			p.communicate()

		if choice == "S":
			p = subprocess.Popen(["powershell.exe",
	            "scripts\\compatchk.ps1"], 
	             stdout=sys.stdout)
			p.communicate()

		if choice == "X":
			exit()



		else:
			longhorn()
longhorn()

