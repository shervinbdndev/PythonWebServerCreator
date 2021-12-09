try:
    import sys
    import socket
    import platform
    import threading
    import webbrowser
    from flask import Flask
    from typing import List
    from time import strftime
    from datetime import date
    from subprocess import run
    from consts import (CONST_COLORS , HOST , PORT , CONTENT_TYPE , ENCODE , HTTP_TYPE)
    from builtins import (str , int ,Exception , open)
    from tkinter import font
    from tkinter.tix import Button
    from tkinter.ttk import (Label , Entry , Notebook , Frame , Combobox)
    from tkinter.__init__ import (Tk , StringVar , Text)
    from tkinter.constants import (RAISED , FLAT , BOTH , CENTER , RIDGE , END)
    from http.server import (BaseHTTPRequestHandler , HTTPServer)

except:
    raise Exception


class StartFlaskServerClass:
    def __init__(self) -> str:
        self.flaskServer = Flask(__name__)


class WebServerCreationClass:
    def __init__(self) -> str:
        super(WebServerCreationClass , self).__init__()
        self.root = Tk()
        self.root.title("WebServer Creator")
        self.root.geometry("{0}x{1}".format(350 , 550))
        self.root.resizable(0 , 0)
        self.root.config(bg = CONST_COLORS[0][0] , cursor = None)
        self.tabDashboard = Notebook(master = self.root)
        self.firstTab = Frame(self.tabDashboard)
        self.secondTab = Frame(self.tabDashboard)
        self.outputTab = Frame(self.tabDashboard)
        self.svEntryPort = StringVar(self.firstTab)
        self.svOptionChs = StringVar(self.firstTab)
        self.sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        self.sock.bind((HOST , PORT))
        self.sock.listen(5)
        self.getTime = strftime("%H:%M:%S %p")
        self.optionChoices : List[str] = [
            "Nginx" ,
            "Ngrok" ,
            "Python http Server" ,
            "Django Server" ,
            "Flask Server" ,
            "Socket Server" ,
            "Default (Socket Server)"
        ]
        self.svEntryPort.set(PORT)
        self.svOptionChs.set(self.optionChoices[5])


        def click_event(param):
            if (param == "click"):
                new_cached = self.textToTemplate.get(1.0 , END)
                with open(r"C:\Users\Shervin\Desktop\Scripts\PythonWebServer\static\index.html" , "w") as F:
                    F.write(new_cached)
                    F.close()
                
                while True:
                    csock , caddr = self.sock.accept()
                    print("Connection From : {0}".format(str(caddr)))

                    req = csock.recv(1024)
                    print(req)

                    csock.sendall(str.encode(HTTP_TYPE , ENCODE))
                    csock.sendall(str.encode(CONTENT_TYPE , ENCODE))
                    csock.sendall(str.encode("\n\r"))

                    with open(r"C:\Users\Shervin\Desktop\Scripts\PythonWebServer\static\index.html" , "r") as R:
                        for i in R.readlines():
                            print("Sent" , repr(i))
                            csock.sendall(str.encode(f" {i} " , ENCODE))
                            continue


        self.tabDashboard.add(
            child = self.firstTab ,
            text = "Config"
        )

        self.tabDashboard.add(
            child = self.secondTab ,
            text = "Mode"
        )

        self.tabDashboard.add(
            child = self.outputTab ,
            text = "Output/Terminal"
        )

        self.firstTabLabel = Label(
            master = self.firstTab ,
            text = None ,
            background = CONST_COLORS[0][0] ,
            width = 82
        )

        self.labelPort = Label(
            master = self.firstTab ,
            text = "Port :" ,
            background = CONST_COLORS[0][0] ,
            foreground = CONST_COLORS[0][1] ,
            font = ("Vani" , 22 , font.BOLD) ,
            relief = FLAT
        )

        self.labelServer = Label(
            master = self.firstTab ,
            text = "Server :" ,
            background = CONST_COLORS[0][0] ,
            foreground = CONST_COLORS[0][1] ,
            font = ("Vani" , 22 , font.BOLD) ,
            relief = FLAT
        )

        self.secondTabLabel = Label(
            master = self.secondTab ,
            text = None ,
            background = CONST_COLORS[0][0] ,
            width = 82
        )

        self.outputtabLabel = Label(
            master = self.outputTab ,
            text = None ,
            background = CONST_COLORS[0][0] ,
            width = 82
        )

        self.entryPort = Entry(
            master = self.firstTab ,
            textvariable = self.svEntryPort ,
            background = CONST_COLORS[0][1] ,
            foreground = CONST_COLORS[0][0] ,
            font = ("Vani" , 13 , font.BOLD) ,
            justify = CENTER ,
            width = 25
        )

        self.optionSelect = Combobox(
            master = self.firstTab ,
            textvariable = self.svOptionChs ,
            values = self.optionChoices ,
            font = ("Vani" , 13 , font.BOLD) ,
            justify = CENTER
        )

        self.htmlLabel = Label(
            master = self.firstTab ,
            text = "HTML" ,
            background = CONST_COLORS[0][0] ,
            foreground = CONST_COLORS[0][1] ,
            font = ("Vani" , 22 , font.BOLD) ,
            relief = RIDGE ,
            borderwidth = 8 ,
            width = 12 ,
            justify = CENTER
        )

        self.textToTemplate = Text(
            master = self.firstTab ,
            width = 36
        )

        self.outputTerminal = Text(
            master = self.outputTab ,
            width = 43 , 
            font = ("Courier" , 15 , font.BOLD) ,
            background = CONST_COLORS[0][3] ,
            foreground = CONST_COLORS[0][2]
        )

        self.outputTerminal.insert(1.0 , f"Date : {date.today()}\nTime : {self.getTime}")

        self.createServerButton = Button(
            master = self.firstTab ,
            text = "Create Server" ,
            command = lambda : click_event("click") ,
            bg = CONST_COLORS[0][4] ,
            fg = CONST_COLORS[0][1] ,
            font = ("Vani" , 15 , font.BOLD) ,
            relief = RAISED ,
            bd = 5
        )

        self.tabDashboard.pack(
            expand = 1 ,
            fill = BOTH
        )

        self.firstTabLabel.place(
            x = 0 ,
            y = 0 ,
            height = 600
        )

        self.secondTabLabel.place(
            x = 0 ,
            y = 0 ,
            height = 600
        )

        self.outputtabLabel.place(
            x = 0 ,
            y = 0 ,
            height = 600
        )

        self.labelPort.place(
            x = 0 ,
            y = 0
        )

        self.labelServer.place(
            x = 0 ,
            y = 60
        )

        self.entryPort.place(
            x = 90 ,
            y = 8
        )

        self.optionSelect.place(
            x = 120 ,
            y = 68
        )

        self.createServerButton.place(
            x = 100 ,
            y = 450
        )

        self.htmlLabel.place(
            x = 78 ,
            y = 110
        )

        self.textToTemplate.place(
            x = 25 ,
            y = 160 ,
            height = 275
        )

        self.outputTerminal.place(
            x = 0 ,
            y = 0 ,
            height = 524
        )

        self.htmlLabel.configure(anchor = CENTER)

        self.root.mainloop()



if (platform.system()[0].upper() == "W"): 
    WebServerCreationClass()
else:
    sys.exit(0)