import subprocess, sys, os, shutil, platform 
from GUI import Window, Button, Label, \
    application
from GUI.Alerts import note_alert, stop_alert, \
    ask, confirm, ask_or_cancel, confirm_or_cancel

def cortana():
	p = subprocess.Popen(["scripts\\delCortana.exe"])
	print("Please run [C] twice for it to take full effect.\n")
	note_alert("Cortana Removed Successfully")


def defaultapps():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\remove-default-apps.ps1"],
		stdout=sys.stdout)
	p.communicate()
	note_alert("Default Apps Removed Successfully")


def defender():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\disable-windows-defender.ps1"],
		stdout=sys.stdout)
	p.communicate()
	note_alert("Windows Defender Disabled Successfully")


def onedrive():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\remove-onedrive.ps1"], 
		stdout=sys.stdout)
	p.communicate()
	note_alert("Onedrive Uninstalled Sucessfully")


def telemetry():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\block-telemetry.ps1"],
		stdout=sys.stdout)
	p.communicate()
	note_alert("Telemetry Blocked Successfully")


def services():
	p = subprocess.Popen(["powershell.exe",
       "scripts\\disable-services.ps1"], 
		stdout=sys.stdout)
	p.communicate()
	note_alert("Intrusive Services Disabled Successfully")


def setup():
	p = subprocess.Popen(["powershell.exe",
    	'-ExecutionPolicy', 
		'Unrestricted',
		"scripts\\setup.ps1"], 
		stdout=sys.stdout)
	p.communicate()
	note_alert("You are now ready to debloat Windows 10")

def wininfo():
	print("----------Windows Info------------")
	import platform as p; print(p.platform());print(p.processor())
	print("----------------------------------")
	note_alert(p.platform())

def winupdate():
	p = subprocess.Popen(["powershell.exe",
       "scripts\\disable-windows-update.ps1"], 
		stdout=sys.stdout)
	p.communicate()

def exit():
	os._exit(0)

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
    Button("Windows Information", action = wininfo),
    Button("Exit Longhorn", action = exit),
]
lbl = Label("""RUN AS ADMIN!
	Longhorn GUI v2.0
	By VincentXII""", position = (20, 50), width = 200)
win.place_column(bt, left = 90 + 200, top = 20)
win.size = (500, 470)
win.add(lbl)

win.show()




application().run()







