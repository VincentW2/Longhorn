# Longhorn Changelog

Longhorn v2.1 - January 12 2019
------------------------------------
### A Whole New Year, A Whole New Look
* Longhorn GUI v2.1 brings a much cleaner layout

#### Old Longhorn GUI
![Old Longhorn Layout](https://upload.vincentxii.us/images/ej0h.png)

#### New Longhorn GUI
![New Longhorn Layout](https://upload.vincentxii.us/images/6l1q.png)

### Under the Hood
* Longhorn GUI is now built with VXGui instead of PyGUI
* Code has been cleaned up

### Misc
* New Longhorn Logo
* Added Changelog
* Added Readme.md in scripts folder regarding delCortana.exe

Longhorn v2.0 - December 9th 2018
------------------------------------
Huge Update. A true milestone.

### The Tale Of Two Versions
* CLI and GUI Version

* CLI Version is left for compatibility reasons, I have no plan for removing it.

### .py ----> .exe
* Finally added compile script for turning longhorn into .exe
 
* Icons are in /lib

* Requires Pyinstaller

### Under The Hood
* Added a delCortana.exe for GUI version

* GUI is written in PyGUI instead of Tkinter (maybe someday have custom fork of PyGUI

* Updated .gitignore to ignore Pyinstaller files

* Compatibility for 1809 confirmed.

Longhorn v1.2 - November 21st 2018
------------------------------------
If the stars align, this will be the last v1.X release of Longhorn. Just had to fix a few bugs.

* Compiled for Windows Executable

* Fixed Cortana Disabling Not Working

Longhorn v1.1 - October 13th 2018
------------------------------------
This is a STABLE release of Longhorn. If you use this release, Longhorn will be fully working but it may be outdated as new commits are pushed.

Improvements Added to 1.1:

* Added Disabling Windows Defender

* Added Windows Image Acquisition service and Handwriting service to disabled services.

Under The Hood:

* Removed un-used scripts

* Added Liability

* Optimized Code

Longhorn v1.0 - October 6th 2018
------------------------------------
This is a STABLE release of Longhorn. If you use this release, Longhorn will be fully working but it may be outdated as new commits are pushed.

1.0 Feature List

* Block Windows Telemetry

* Disable Intrusive Services

* Remove Cortana

* Remove Default Apps

* Remove Onedrive

* Setup Powershell to run files (also known as Setting up Longhorn)