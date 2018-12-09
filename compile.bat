echo Compiling Longhorn CLI and GUI vesions to .exe.......
pyinstaller -y -F -i "lib/longhorn_gui.ico"  "longhorn-gui.py"
pyinstaller -y -F -i "lib/longhorn_cli.ico"  "longhorn-cli.py"
xcopy dist\longhorn-gui.exe
xcopy dist\longhorn-cli.exe 
echo Done Compiling