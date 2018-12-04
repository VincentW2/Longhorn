import subprocess, sys, os, shutil, platform
from GUI import Window, Button, Label, RadioGroup, RadioButton, \
    application
from GUI.Alerts import alert, alert2, alert3, note_alert, stop_alert, \
    ask, confirm, ask_or_cancel, confirm_or_cancel


print("If you see this, running it works.")

def cortana():
	p = subprocess.Popen(["scripts\\delCortana.exe"])
	print("Please run [C] twice for it to take full effect.\n")

def defaultapps():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\remove-default-apps.ps1"],
		stdout=sys.stdout)
	p.communicate()

def defender():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\disable-windows-defender.ps1"],
		stdout=sys.stdout)
	p.communicate()

def onedrive():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\remove-onedrive.ps1"], 
		stdout=sys.stdout)
	p.communicate()

def telemetry():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\block-telemetry.ps1"],
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

def wininfo():
	print("----------Windows Info------------")
	import platform as p; print(p.platform());print(p.processor())
	print("----------------------------------")

def winupdate():
	p = subprocess.Popen(["powershell.exe",
       "scripts\\disable-windows-update.ps1"], 
		stdout=sys.stdout)
	p.communicate()

def exit():
	exit()

win = Window(title = "Longhorn v2.0")
bt = [
    Button("Disable Cortana", action = cortana),
    Button("Remove Default Apps", action = defaultapps),
    Button("Disable Windows Defender", action = defender),
    Button("Remove Onedrive", action = onedrive),
    Button("Block Telemetry", action = telemetry),
    Button("Disable Intrusive Services", action = services),
    Button("Setup Longhorn", action = setup),
    Button("Disable Windows Update", action = winupdate),
    Button("Exit Longhorn", action = exit),
]
lbl = Label("""Longhorn v2.0
	By VincentXII""", position = (20, 50), width = 200)
win.place_column(bt, left = 90 + 200, top = 20)
win.size = (500, 470)
win.add(lbl)

win.show()




application().run()







