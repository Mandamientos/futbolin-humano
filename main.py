import threading
import time
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import serial

# Abrir el puerto donde está conectada la Raspberry

#ser = serial.Serial(port='COM3', baudrate=10000)

# Menú principal función crear el menú prinicipal
def mainMenu(window_width, window_height, Logo):

    root.title("Menú Principal")
    
    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    container.pack()
    container.create_image(620, 300, image=Logo)

    playButton = Button(container, font=("Champions", 35), text="JUGAR", command=lambda:[container.destroy(), initConfig(window_width, window_height)])
    playButton.place(x=520, y=500)

    aboutButton = Button(container, font=("Champions", 35), text="ACERCA")
    aboutButton.place(x=510, y=650)

    verLabel = Label(container, font=("Champions", 25), text="VERSIÓN 1.0", bg="#14223E", fg="#FFFFFF")
    verLabel.place(x=20, y=950)


# Menú configuración inicial
def initConfig(window_width, window_height):

    global logoMCI, logoRMA

    root.title("Configuración inicial")

    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    container.pack()

    configTitle = Label(container, font=("Champions", 40), text="CONFIGURACIÓN INICIAL", bg="#14223E", fg="#FFFFFF")
    configTitle.place(x=30, y=30)

    pickTitle = Label(container, font=("ITC Novarese Std Medium", 30), text="ESCOJA DOS EQUIPOS", bg="#14223E", fg="#FFFFFF")
    pickTitle.place(x=380, y=250)

    MCIButton = Button(container, image=logoMCI, background="#14223E", state="normal", command=lambda:[choosenTeams(MCIButton, "Manchester City", container)])
    MCIButton.place(x=100, y=400)

    RMAButton = Button(container, image=logoRMA, background="#14223E", width=250, state="normal", command=lambda:[choosenTeams(RMAButton, "Real Madrid", container)])
    RMAButton.place(x=450, y=400)

    BARButton = Button(container, image=logoBAR, background="#14223E", width=250, state="normal", command=lambda:[choosenTeams(BARButton, "Barcelona FC", container)])
    BARButton.place(x=800, y=400)


# Guarda qué equipos escogió el usuario.
def choosenTeams(button, teamName, container):
    global firstTeam, secondTeam
    if firstTeam == None:
        button["state"] = "disabled"
        firstTeam = f"{teamName}"
    elif secondTeam == None:
        button["state"] = "disabled"
        secondTeam = f"{teamName}"
        startButton = Button(container, font=("Champions", 40), text="SIGUIENTE", command=lambda:[container.destroy(), decideSides()]).place(x=440, y=800)
    else:
        pass

# Decide quien es el local y quien el visitante
def decideSides():
    global local, visiting
    teams = [firstTeam, secondTeam]
    local = random.choice(teams)
    del teams[teams.index(local)]
    visiting = teams[0]
    print("Local:", local, "\nVisitante:", visiting)

# def readPico():
#     global ser, datos
#     while True:
#         data = ser.readline()
#         if (data.decode("UTF-8").strip())[0] == '>':
#             pass
#         else:
#             datos.add(data.decode("UTF-8").strip())
#         print(datos)
#
# def sendPico():
#         dato = "hola()\r\n"
#         ser.write(dato.encode())

root = Tk()

window_width = 1200
window_height = 1000

root.geometry(f"{window_width}x{window_height}")
root.resizable(width=False, height=False)
root.config(background="#14223E")

# Imágenes de la interfaz

openLogo = Image.open("assets/logo.png")
Logo = ImageTk.PhotoImage(openLogo.resize((1000, 1000)))

logoMCIOp = Image.open("assets/LogoMCI.png")
logoMCI = ImageTk.PhotoImage(logoMCIOp.resize((250, 250)))

logoRMAOp = Image.open("assets/LogoRMA.png")
logoRMA = ImageTk.PhotoImage(logoRMAOp.resize((200, 250)))

logoBAROp = Image.open("assets/logoBAR.png")
logoBAR = ImageTk.PhotoImage(logoBAROp.resize((250, 250)))

# Variables para el funcionamiento del juego

datos = set()
firstTeam = None
secondTeam = None
local = None
visiting = None

#threadPicoRead = threading.Thread(target=readPico)
#threadPicoRead.start()

#threadPicoSend = threading.Thread(target=sendPico)
#threadPicoSend.start()

mainMenu(window_width, window_height, Logo)

root.mainloop()