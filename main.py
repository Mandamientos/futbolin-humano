from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random


# Menú principal función crear el menú prinicipal
def mainMenu(window_width, window_height, Logo):
    containter = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    containter.pack()
    containter.create_image(620, 300, image=Logo)

    playButton = Button(containter, font=("Champions", 35), text="JUGAR")
    playButton.place(x=520, y=500)

    aboutButton = Button(containter, font=("Champions", 35), text="ACERCA")
    aboutButton.place(x=510, y=650)

    verLabel = Label(containter, font=("Champions", 25), text="VERSIÓN 1.0", bg="#14223E", fg="#FFFFFF")
    verLabel.place(x=20, y=950)

root = Tk()

window_width = 1200
window_height = 1000

root.geometry(f"{window_width}x{window_height}")
root.resizable(width=False, height=False)
root.config(background="#14223E")

# Imágenes de la interfaz

openLogo = Image.open("assets/logo.png")
Logo = ImageTk.PhotoImage(openLogo.resize((1000, 1000)))


mainMenu(window_width, window_height, Logo)

root.mainloop()