running=True
exit_aliases=["pythoncmd","quit","exit"]
clear_aliases=["clear","cls"]
commands=["help","about","windows","python","echo","speedtest"]
print("Welcome to PythonCMD!")

while running==True:
    def help(): # Help
        print("help - Displays this help dialog\nabout - Displays some info around PythonCMD\nwindows - Switch to Windows CMD Mode so you can use Windows commands within PythonCMD\npython - Switch to Python CLI Mode in order to execute any python command as if you weren't running anything\necho - Broadcast your message\nspeedtest - Test your internet connection (requires speedtest-cli library)\ncls / clear - Clear Python shell (only works on Python shell running on Windows)")
    
    def about(): # About PythonCMD
        print("PythonCMD is a Python-based command prompt concept with lots of useful commands and has the goal to simulate the Windows command prompt feeling into Python.")
    
    def windows(): # Windows CMD Mode (ONLY AVAILABLE IN WINDOWS)
        import os
        windowsmode=True
        print("Welcome to PythonCMD Windows Mode!\n\nTo exit Windows Mode, type *pythoncmd*")
        while windowsmode==True:
            wincommand=input("WindowsMode>")
            if wincommand in exit_aliases:
                windowsmode=False
                print("Exited Windows CMD Mode")
            else:
                os.system(wincommand)
    
    def python(): # Python CLI Mode
        pythonmode=True
        print("Welcome to Python CLI Mode!\n\nTo exit Python CLI Mode, type *pythoncmd*")
        while pythonmode==True:
            pycommand=input(">>>")
            if pycommand in exit_aliases:
                pythonmode=False
                print("Exited Python CLI Mode")
            elif pycommand in globals():
                print("To use these commands, exit Python CLI Mode (pythoncmd) and try again.")
            elif pycommand=="":
                print("No input provided.")
            else:
                try:
                    eval(pycommand)
                except:
                    print("Syntax error! Fix it.")
    
    def echo(): # Echo message
        echo=input("Echo your message: ")
        prompt=1
        while prompt==1:
            clear_prompt=input("Do you want to clear the window before echoing? y (Yes) or n (No)? ")
            if clear_prompt=="y":
                clear()
                prompt=0
            elif clear_prompt=="n":
                prompt=0
        print(echo)
    
    def clear(): # Clear shell
        try:
            import os
            clear_command="cls"
            os.system(clear_command)
        except:
            for i in range(1000):
                print("")
    
    def speedtest(): # Speedtest internet connection
        try:
            import speedtest
        except:
            print("speedtest-cli not found. Downloading...")
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", "speedtest-cli"])
            clear()
            import speedtest
        speed=speedtest.Speedtest()
        servers=[]
        speed.get_servers(servers)
        speed.get_best_server()
        print("Ping:", int(speed.results.ping))
        print("Download Speed:", (int(speed.download() / 1000000)), "Mbps")
        print("Upload Speed:", (int(speed.upload() / 1000000)), "Mbps")

    command=input(">>>") # PythonCMD input
    
    # if CONDITIONS
    
    if command in commands:
        result=eval(command+"()")
    elif command in clear_aliases:
        result=eval("clear()")
    elif command=="pythoncmd":
        print("You have to be in Windows CMD Mode (Command: windows) or Python CLI Mode (Command: python) in order to execute this command!")
    elif command=="":
        print("Type a command.")
    else:
        print("Invalid command! For reference, type *help* to see all available commands.")
