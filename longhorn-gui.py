from GUI import Window, Button, RadioGroup, RadioButton, \
    application
from GUI.Alerts import alert, alert2, alert3, note_alert, stop_alert, \
    ask, confirm, ask_or_cancel, confirm_or_cancel


print("If you see this, running it works.")

def defaultapps():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\remove-default-apps.ps1"],
		stdout=sys.stdout)
	p.communicate()

def telemetry():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\block-telemetry.ps1"],
		stdout=sys.stdout)
	p.communicate()

def cortana():
	p = subprocess.Popen(["scripts\\delCortana.exe"])
	print("Please run [C] twice for it to take full effect.\n")

def defender():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\disable-windows-defender.ps1"],
		stdout=sys.stdout)
	p.communicate()

def wininfo():
	print("----------Windows Info------------")
	import platform as p; print(p.platform());print(p.processor())
	print("----------------------------------")

def ondrive():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\remove-onedrive.ps1"], 
		stdout=sys.stdout)
	p.communicate()

def services():
	p = subprocess.Popen(["powershell.exe",
       "scripts\\disable-services.ps1"], 
		stdout=sys.stdout)
	p.communicate()

def setup():
	p = subprocess.Popen(["powershell.exe",
    	'-ExecutionPolicy', 
		'Unrestricted',
		"scripts\\setup.ps1"], 
		stdout=sys.stdout)
	p.communicate()

def winupdate():
	p = subprocess.Popen(["powershell.exe",
       "scripts\\disable-windows-update.ps1"], 
		stdout=sys.stdout)
	p.communicate()

def exit():
	exit()

win = Window(title = "Longhorn v2.0")



win.show()




application().run()







