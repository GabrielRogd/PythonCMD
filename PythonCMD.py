running=True
exit_aliases=["pythoncmd","quit","exit"]
clear_aliases=["clear","cls"]
commands=["help","about","windows","python","echo","speedtest","notepad","weather","winupdate"]
print("Welcome to PythonCMD!")

while running==True:
    def help(): # Help
        print("help - Displays this help dialog\nabout - Displays some info around PythonCMD\nwindows - Switch to Windows CMD Mode so you can use Windows commands within PythonCMD\npython - Switch to Python CLI Mode in order to execute any python command as if you weren't running anything\necho - Broadcast your message\nspeedtest - Test your internet connection (requires speedtest-cli library)\ncls / clear - Clear Python shell (only works on Python shell running on Windows)\nwinupdate - Effortlessly disable Windows Updates (use at your own risk, requires Windows host)\n")
    
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
            elif any(word in pycommand for word in commands) and pycommand.endswith("()"):
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
            range(1000)(print("\n"))
    
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
        print("Selected server:", speed.results.server["sponsor"])
        print("Ping:", int(speed.results.ping))
        print("Download Speed:", (int(speed.download() / 1000000)), "Mbps")
        print("Upload Speed:", (int(speed.upload() / 1000000)), "Mbps")

    def winupdate(): # Windows update disabler. ONLY AVAILABLE IN WINDOWS
        update_menu=True
        import ctypes, sys
        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
        if is_admin():
            print("You are running PythonCMD as administrator.")
            print("Do you want to disable Windows Updates? y (Yes) or n (No)?")
            print("If you care about your computer's security, don't use this option further. Type n (No) to exit.")
            while update_menu==True:
                disable_updates=input(">>>")
                if disable_updates=="y":
                    import os
                    os.system("sc config wuauserv start= disabled")
                    print("Windows Updates have been disabled.")
                    update_menu=False
                elif disable_updates=="n":
                    print("Windows Updates have not been disabled. Exiting Windows Update menu...")
                    update_menu=False
                else:
                    print("Invalid input.")
        else:
            print("You are not running PythonCMD as administrator.")
            print("PythonCMD will be closed and relaunched with administrator rights.")
            print("Press enter, launch as admin, then type *winupdate* again to continue.")
            print("Type *pythoncmd* to exit Windows Update menu.")
            choice=input()
            if choice=="":
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sys.exit()
            while update_menu==True:
                if choice in exit_aliases:
                    update_menu=False
                    print("Exited Windows Update menu.")


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
    elif command in exit_aliases:
        running=False
    else:
        print("Invalid command! For reference, type *help* to see all available commands.")
