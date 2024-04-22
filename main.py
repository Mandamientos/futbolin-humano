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
    
    containter = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    containter.pack()
    containter.create_image(620, 300, image=Logo)

    playButton = Button(containter, font=("Champions", 35), text="JUGAR", command=sendPico)
    playButton.place(x=520, y=500)

    aboutButton = Button(containter, font=("Champions", 35), text="ACERCA")
    aboutButton.place(x=510, y=650)

    verLabel = Label(containter, font=("Champions", 25), text="VERSIÓN 1.0", bg="#14223E", fg="#FFFFFF")
    verLabel.place(x=20, y=950)

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

# Variables para el funcionamiento del juego

datos = set()

threadPicoRead = threading.Thread(target=readPico)
threadPicoRead.start()

#threadPicoSend = threading.Thread(target=sendPico)
#threadPicoSend.start()

mainMenu(window_width, window_height, Logo)

root.mainloop()