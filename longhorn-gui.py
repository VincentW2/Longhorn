import subprocess, sys, os, shutil, platform 
from VXGUI.StdColors import red
from VXGUI.Geometry import offset_rect, rect_sized
from VXGUI import Window, Image, View, Button, Label, application
from VXGUI.Alerts import note_alert

## Commands ##
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

## The Buttons ##
win = Window(title = "Longhorn v2.1")
bt = [
    Button("Disable Cortana", action = cortana),
    Button("Remove Default Apps", action = defaultapps),
    Button("Disable Windows Defender", action = defender),
    Button("Remove Onedrive", action = onedrive),
    Button("Block Telemetry", action = telemetry),
    Button("Disable Intrusive Services", action = services),
    Button("Disable Windows Update", action = winupdate),
]
bt2 = [
    Button("Setup Longhorn", action = setup),
    Button("Windows Information", action = wininfo),
    Button("Exit Longhorn", action = exit),
]

class ImageTestView(View):

    def draw(self, c, r):
        #c.backcolor = yellow
        c.erase_rect(r)
        main_image_pos = (0, 0)
        src_rect = (image.bounds)
        dst_rect = offset_rect(src_rect, main_image_pos)
        image.draw(c, src_rect, dst_rect)


## Label and Image Placement ##
runadminlbl = Label("RUN AS ADMIN!", color = red, position = (500, 340), width = 200)
image_path = "lib/longhorn-2.1.png"
image = Image(file = image_path)
view = ImageTestView(size = (800,278))
win.add(view)

## Actually building the window ##
win.place_column(bt, left = 200, top = 330)
win.place_column(bt2, left = 500, top = 370)
win.size = (800, 570)
win.add(runadminlbl)
win.show()
application().run()
