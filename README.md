# PythonCMD
A Python-based command prompt concept which includes Windows (and Python) command emulation.

Current features:
- echo: Input your message and it will be clearly outputted in Python
- windows (CMD Mode): Emulate Windows commands that you would normally write in a Windows CMD (Requires Windows host); kind of like a command prompt within a command prompt within a shell
- python: Switch to a Python CLI environment so you can execute Python commands freely (In case of any syntax error, PythonCMD has a failsafe in place and will not crash but will instead output syntax error)
- speedtest: Test your internet connection (requires speedtest-cli library)
- cls / clear - Clear Python shell (only works on Python shell running on Windows)
- winupdate - Disable Windows Update services (wuauserv service) effortlessly. In this case, PythonCMD can automatically re-launch with administrator rights which is necessary to disable the service (Requires Windows host)

If you miss out on libraries that are necessary to run some commands, don't worry! They will automatically be downloaded through pip. Hence there's no requirements.txt file :)

This project is at an early stage, meaning that soonly more features will be added!

Tested in Python 3.12.

Licensed with MIT License. You are permitted to use this script commercially or personally, as well as able to fork in case of improvements and/or added features.
