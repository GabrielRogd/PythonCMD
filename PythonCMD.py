running=True
print("Welcome to PythonCMD!")
while running==True:
    def help():
        print("help - Displays this help dialog\nabout - Displays some info around PythonCMD\nwindows - Switch to Windows CMD Mode so you can use Windows commands within PythonCMD (Upon command execution, a second shell will be opened to execute the command)\npythoncmd - Switch to PythonCMD mode (You have to be in Windows CMD Mode in order to execute this command")
    def about():
        print("PythonCMD is a Python-based command prompt concept with lots of useful commands and has the goal to simulate the Windows command prompt feeling into Python.")
    def windows():
        import os
        windowsmode=True
        print("Welcome to PythonCMD Windows Mode!\n\nTo exit Windows Mode, type *pythoncmd*")
        while windowsmode==True:
            wincommand=input("WindowsMode>")
            if wincommand=="pythoncmd":
                windowsmode=False
                print("Exited Windows CMD Mode")
            else:
                os.system(wincommand)
    def echo():
        echo=input("Echo your message: ")
        for i in range(51):
            print(" ")
        print(echo)
    def cls():
        for i in range(101):
            print(" ")
    def speedtest():
        import webbrowser
        speedtest=input("Choose your desired speedtesting platform (speedtest.net, fast.com): ")
        if speedtest=="Speedtest.net" or speedtest=="speedtest.net" or speedtest=="SPEEDTEST.NET" or speedtest=="Ookla" or speedtest=="ookla" or speedtest=="OOKLA" or speedtest=="Speedtest" or speedtest=="speedtest" or speedtest=="SPEEDTEST":
            url="speedtest.net"
            webbrowser.open_new(url)
        elif speedtest=="Fast.com" or speedtest=="fast.com" or speedtest=="FAST.COM" or speedtest=="Fast" or speedtest=="fast" or speedtest=="FAST":
            url="fast.com"
            webbrowser.open_new(url)
        else:
            url=speedtest
            webbrowser.open_new(url)
    command=input(">>>")
    if command=="help" or command=="about" or command=="windows" or command=="echo" or command=="cls" or command=="speedtest":
        result=eval(command+"()")
    elif command=="pythoncmd":
        print("You have to be in Windows CMD Mode (Command: windows) in order to execute this command!")
    elif command=="":
        print("Type a command.")
    else:
        print("Invalid command!")
