import subprocess, sys, os, shutil, platform 
from VXGUI.StdColors import blue
from VXGUI.Geometry import offset_rect, rect_sized
from VXGUI import Window, Image, View, Button, Label, application, Font
from VXGUI.Alerts import note_alert

## Commands ##
def about():
	note_alert("""Longhorn is a Windows Debloater made by VincentXII.\n
Please read the included "README.md" for more information on Longhorn""")

def changelog():
	p = subprocess.Popen(["notepad.exe",
		"CHANGELOG.md"],
		stdout=sys.stdout)

def cortana():
	p = subprocess.Popen(["scripts\\delCortana.bat"])
	p = subprocess.Popen(["scripts\\delCortana.bat"])
	p = subprocess.Popen(["scripts\\delCortana.bat"])
	note_alert("Cortana Removed Successfully")

def defaultapps():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\remove-default-apps.ps1"],
		stdout=sys.stdout)
	p.communicate()
	note_alert("Default Apps Removed Successfully")

def defender():
	note_alert("Please run this once, restart, and run this again for it to work.")
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

def restorepoint():
	p = subprocess.Popen(["powershell.exe",
		"scripts\\create-restore-point.ps1"],
		stdout=sys.stdout)
	p.communicate()
	note_alert("Created Restore Point")

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
	note_alert("Longhorn Succesfully Setup")

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

## The Buttons ##
win = Window(title = "Łonghorn v3.1 FINAL")
longhorn = [
    Button("Disable Cortana", action = cortana),
    Button("Remove Default Apps", action = defaultapps),
    Button("Disable Windows Defender", action = defender),
    Button("Remove Onedrive", action = onedrive),
    Button("Block Telemetry", action = telemetry),
    Button("Disable Intrusive Services", action = services),
    Button("Disable Windows Update", action = winupdate),
]
misc = [
    Button("Setup Longhorn", action = setup),
    Button("Windows Information", action = wininfo),
    Button("Create Restore Point", action = restorepoint),
]
info = [
	Button("About Longhorn", action = about),
	Button("Changelog", action = changelog),
	Button("Exit Longhorn", action = exit),
]
class LonghornHeaderImageDisplay(View):

    def draw(self, c, r):

        c.erase_rect(r)
        main_image_pos = (0, 0)
        src_rect = (image.bounds)
        dst_rect = offset_rect(src_rect, main_image_pos)
        image.draw(c, src_rect, dst_rect)

## Label and Image Placement ##
longhornbt = Label("Longhorn Features", color = blue, position = (50, 300))
miscbt = Label("Miscellaneous", color = blue, position = (300, 340))
infobt = Label("Information", color = blue, position = (500, 340))

image_path = "lib/longhorn-3.0.png"
image = Image(file = image_path)
view = LonghornHeaderImageDisplay(size = (800,278))
win.add(view)

## Deprecation Statement ##
depalert = Window(title = "Attention!")
class DepAlertDisplay(View):

    def draw(self, d, e):

        d.erase_rect(e)
        main_image_pos2 = (0, 0)
        src_rect2 = (imagedep.bounds)
        dst_rect2 = offset_rect(src_rect2, main_image_pos2)
        imagedep.draw(d, src_rect2, dst_rect2)
image_path2 = "lib/depalert.png"
imagedep = Image(file = image_path2)
viewdep = DepAlertDisplay(size = (500,375))
depalert.add(viewdep)
## Actually building the window ##
win.place_column(longhorn, left = 50, top = 330)
win.place_column(misc, left = 300, top = 370)
win.place_column(info, left = 500, top = 370)
win.size = (800, 570)
win.add(longhornbt)
win.add(miscbt)
win.add(infobt)
win.show()
depalert.size = (500,375)
depalert.show()
application().run()
