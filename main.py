import threading
import time
from tkinter import *
from PIL import Image, ImageTk
import random
import pygame
import socket
import os
import natsort
import json

def mainMenu(window_width, window_height, Logo):

    root.title("Menú Principal")
    
    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    container.pack()
    container.create_image(600, 500, image=Stars)
    container.create_image(620, 300, image=Logo)

    playButton = Button(container, font=("Champions", 35), text="JUGAR", command=lambda:[container.destroy(), initConfig(window_width, window_height)])
    playButton.place(x=520, y=500)

    aboutButton = Button(container, font=("Champions", 35), text="ACERCA", command=lambda :[container.destroy(), aboutMenu()])
    aboutButton.place(x=510, y=750)

    stadisticsBtn = Button(container, font=("Champions", 35), text="ESTADÍSTICAS", command=lambda:[container.destroy(), stadisticsMenu("Manchester City", "MCI")])
    stadisticsBtn.place(x=450, y=625)

    testModulesBtn = Button(container, font=("Champions", 35), text="PROBAR", command=lambda:[container.destroy(), testMenu(window_width, window_height)]) #testMenu(window_width, window_height)
    testModulesBtn.place(x=970, y=870)

    verLabel = Label(container, font=("Champions", 25), text="VERSIÓN 1.1", bg="#14223E", fg="#FFFFFF")
    verLabel.place(x=20, y=20)


def aboutMenu():
    global LogoTEC
    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    container.pack()

    container.create_image(600, 200, image=LogoTEC)

    etiqueta = Label(container,
                        text="Autores: Guillermo Sanchez, Johnny Alfaro\n Fundamentos de Sistemas Computacionales\n Ingenieria en Computadores\n 2024 \n Profesor: Jason Leiton\n Creado en Costa Rica \n Version 1.1 \n  ",
                     background="#14223E",
                     fg="#FFFFFF",
                     font=("Champions", 35))
    etiqueta.place(x=150, y=400)

    backBtn = Button(root, font=("Champions", 35), text="VOLVER", bg="#3562A6", fg="#FFFFFF",
                 command=lambda: [container.destroy(), mainMenu(window_width, window_height, Logo)])
    backBtn.place(x=1000, y=900)

def stadisticsMenu(team, sig):
    global logoMCI_est, logoBAR_est, logoRMA_est, totalGoals, totalSaves, totalFailed, topStriker, strikerList, keeperList
    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    container.pack()

    backBtn = Button(root, font=("Champions", 35), text="VOLVER", bg="#3562A6", fg="#FFFFFF", command=lambda:[container.destroy(), mainMenu(window_width, window_height, Logo)])
    backBtn.place(x=1000, y=900)

    root.title("Estadísticas")

    nav = Canvas(container, height=1200, width=300, background="#3562A6", highlightbackground="#3562A6")
    nav.place(x=0, y=0)

    titleLabel = Label(nav, font=("Champions", 35), text="Equipos", bg="#3562A6", fg="#FFFFFF")
    titleLabel.place(x=75, y=20)

    estMCI = Button(nav, image=logoMCI_est, state="normal", command=lambda :[container.destroy(), stadisticsMenu("Manchester City", "MCI")])
    estMCI.place(x=50, y=100)

    estRMA = Button(nav, image=logoRMA_est, width=200, state="normal", command=lambda :[container.destroy(), stadisticsMenu("Real Madrid","RMA")])
    estRMA.place(x=50, y=400)

    estBAR = Button(nav, image=logoBAR_est, state="normal", command=lambda :[container.destroy(), stadisticsMenu("Barcelona FC","BAR")])
    estBAR.place(x=50, y=700)

    if team == "Manchester City":
        estMCI["state"] = "disabled"
    elif team == "Real Madrid":
        estRMA["state"] = "disabled"
    elif team == "Barcelona FC":
        estBAR["state"] = "disabled"

    ##################################################################################

    teamName = StringVar()
    teamName.set(f"Estadísiticas generales del {team}")

    manageGeneralStadistics(team)

    teamTittle = Label(container, font=("Champions", 35), textvariable=teamName, bg="#14223E", fg="#FFFFFF", width=36, anchor="n")
    teamTittle.place(x=320, y=20)

    totalGoalsLabel = Label(container, font=("ITC Novarese Std Medium", 30), textvariable=totalGoals, bg="#14223E", fg="#6594C0")
    totalGoalsLabel.place(x=320, y=130)

    totalSavesLabel = Label(container, font=("ITC Novarese Std Medium", 30), textvariable=totalSaves, bg="#14223E", fg="#6594C0")
    totalSavesLabel.place(x=320, y=180)

    totalFailedLabel = Label(container, font=("ITC Novarese Std Medium", 30), textvariable=totalFailed, bg="#14223E", fg="#6594C0")
    totalFailedLabel.place(x=320, y=230)

    topStrikerLabel = Label(container, font=("ITC Novarese Std Medium", 30), textvariable=topStriker, bg="#14223E", fg="#6594C0")
    topStrikerLabel.place(x=320, y=280)

    individualTittle = Label(container, font=("Champions", 35), text="Estadísticas Individuales", bg="#14223E", fg="#FFFFFF", width=36, anchor="n")
    individualTittle.place(x=320, y=400)

    listajugadores = os.listdir(f"{team}/jugadores-{sig}")
    listaporteros = os.listdir(f"{team}/porteros-{sig}")
    jugadoresImgs = []
    porterosImgs = []

    for i in listajugadores:
        id = Image.open(f"{team}/jugadores-{sig}/{i}")
        jugadoresImgs.append(ImageTk.PhotoImage(id.resize((250,250))))
    for i in listaporteros:
        id = Image.open(f"{team}/porteros-{sig}/{i}")
        porterosImgs.append(ImageTk.PhotoImage(id.resize((250,250))))

    player1btn = Button(container, image=jugadoresImgs[0], command=lambda:[manageIndividualStats(team, strikerList[0][0], jugadoresImgs[0], 0, "striker"), container.destroy()])
    player1btn.place(x=340, y=500)

    player2btn = Button(container, image=jugadoresImgs[1], command=lambda:[manageIndividualStats(team, strikerList[1][0], jugadoresImgs[1], 1, "striker"), container.destroy()])
    player2btn.place(x=620, y=500)

    player3btn = Button(container, image=jugadoresImgs[2], command=lambda:[manageIndividualStats(team, strikerList[2][0], jugadoresImgs[2], 2, "striker"), container.destroy()])
    player3btn.place(x=900, y=500)

    nextbtn = Button(container, font=("Champions", 30), text=">>>>", command=lambda: [loadImgs(jugadoresImgs, porterosImgs, container, "nxt", team), player1btn.destroy(), player2btn.destroy(), player3btn.destroy(), nextbtn.destroy()])
    nextbtn.place(x=690,y=800)

    root.mainloop()

def loadImgs(jugadoresImgs, porterosImgs, container, mode, team):
    if mode == "nxt":

        nextbtn = Button(container, font=("Champions", 30), text="<<<<",
                         command=lambda: [loadImgs(jugadoresImgs, porterosImgs, container, "prev", team),
                                          player4btn.destroy(), player5btn.destroy(), player6btn.destroy(), nextbtn.destroy()])
        nextbtn.place(x=690, y=800)

        player4btn = Button(container, image=jugadoresImgs[3], command=lambda:[manageIndividualStats(team, strikerList[3][0], jugadoresImgs[3], 3, "striker"), container.destroy()])
        player4btn.place(x=340, y=500)

        player5btn = Button(container, image=porterosImgs[0], command=lambda:[manageIndividualStats(team, keeperList[0][0], porterosImgs[0], 0, "keeper"), container.destroy()])
        player5btn.place(x=620, y=500)

        player6btn = Button(container, image=porterosImgs[1], command=lambda:[manageIndividualStats(team, keeperList[1][0], porterosImgs[1], 1, "keeper"), container.destroy()])
        player6btn.place(x=900, y=500)

    if mode == "prev":
        nextbtn = Button(container, font=("Champions", 30), text=">>>>",
                         command=lambda: [loadImgs(jugadoresImgs, porterosImgs, container, "nxt", team),
                                          player1btn.destroy(), player2btn.destroy(), player3btn.destroy(),
                                          nextbtn.destroy()])
        nextbtn.place(x=690, y=800)

        player1btn = Button(container, image=jugadoresImgs[0], command=lambda:[manageIndividualStats(team, strikerList[0][0], jugadoresImgs[0], 0, "striker"), container.destroy()])
        player1btn.place(x=340, y=500)

        player2btn = Button(container, image=jugadoresImgs[1], command=lambda:[manageIndividualStats(team, strikerList[1][0], jugadoresImgs[1], 1, "striker"), container.destroy()])
        player2btn.place(x=620, y=500)

        player3btn = Button(container, image=jugadoresImgs[2], command=lambda: [
            manageIndividualStats(team, strikerList[2][0], jugadoresImgs[2], 2, "striker"), container.destroy()])
        player3btn.place(x=900, y=500)


def manageGeneralStadistics(team):
    global totalGoals, totalSaves, totalFailed, topStriker, strikerList, keeperList
    print(team)
    with open("teams-data-base.json", encoding="utf-8") as f:
        datos = json.load(f)

    strikerList = []
    keeperList = []

    for Teams in datos["Teams"]:
        if Teams["Team"] == team:
            for Player in Teams["Strikers"]:
                strikerList.append([Player["Name"], Player["Goals"], Player["Failed"]])
            for Player in Teams["Keepers"]:
                keeperList.append([Player["Name"], Player["Saves"], Player["Failed"]])

    strikerListSorted = natsort.natsorted(strikerList, key=lambda x:x[1], reverse=True)
    keeperListSorted = natsort.natsorted(keeperList, key=lambda x:x[1], reverse=True)

    topStriker.set(f" • Goleador: {strikerListSorted[0][0]}")

    totalG = 0
    totalF = 0
    totalS = 0

    for i in range(len(strikerListSorted)):
        totalG += int(strikerListSorted[i][1])
        totalF += int(strikerListSorted[i][2])
    for i in range(len(keeperListSorted)):
        totalS += int(keeperListSorted[i][1])

    totalGoals.set(f" • Goles totales: {totalG}")
    totalFailed.set(f" • Goles fallados: {totalF}")
    totalSaves.set(f" • Atajadas totales: {totalS}")


def manageIndividualStats(team, player, img, i, mode):
    global logoMCI_est, logoBAR_est, logoRMA_est, strikerList, keeperList

    def back():
        if team == "Manchester City":
            stadisticsMenu("Manchester City", "MCI")
        elif team == "Real Madrid":
            stadisticsMenu("Real Madrid", "RMA")
        elif team == "Barcelona FC":
            stadisticsMenu("Barcelona FC", "BAR")

    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    container.pack()

    backBtn = Button(root, font=("Champions", 35), text="ATRÁS", bg="#3562A6", fg="#FFFFFF", command=lambda:[container.destroy(), back()])
    backBtn.place(x=1000, y=900)

    root.title("Estadísticas")

    nav = Canvas(container, height=1200, width=300, background="#3562A6", highlightbackground="#3562A6")
    nav.place(x=0, y=0)

    titleLabel = Label(nav, font=("Champions", 35), text="Equipos", bg="#3562A6", fg="#FFFFFF")
    titleLabel.place(x=75, y=20)

    estMCI = Button(nav, image=logoMCI_est, state="normal", command=lambda :[container.destroy(), stadisticsMenu("Manchester City", "MCI")])
    estMCI.place(x=50, y=100)

    estRMA = Button(nav, image=logoRMA_est, width=200, state="normal", command=lambda :[container.destroy(), stadisticsMenu("Real Madrid","RMA")])
    estRMA.place(x=50, y=400)

    estBAR = Button(nav, image=logoBAR_est, state="normal", command=lambda :[container.destroy(), stadisticsMenu("Barcelona FC","BAR")])
    estBAR.place(x=50, y=700)

    if team == "Manchester City":
        estMCI["state"] = "disabled"
    elif team == "Real Madrid":
        estRMA["state"] = "disabled"
    elif team == "Barcelona FC":
        estBAR["state"] = "disabled"

    ###############################################################################################

    if mode == "striker":

        strikerTitle = Label(container, font=("Champions", 35), text=f"Estadísiticas de {player}", bg="#14223E", fg="#FFFFFF", width=36, anchor="n")
        strikerTitle.place(x=320, y=20)

        totalGoalsLabel = Label(container, font=("ITC Novarese Std Medium", 30), text=f" • Goles totales: {strikerList[i][1]}", bg="#14223E", fg="#6594C0")
        totalGoalsLabel.place(x=320, y=130)

        totalFailedLabel = Label(container, font=("ITC Novarese Std Medium", 30), text=f" • Tiros fallados: {strikerList[i][2]}", bg="#14223E", fg="#6594C0")
        totalFailedLabel.place(x=320, y=230)

    elif mode == "keeper":

        keeperTitle = Label(container, font=("Champions", 35), text=f"Estadísiticas de {player}", bg="#14223E", fg="#FFFFFF", width=36, anchor="n")
        keeperTitle.place(x=320, y=20)

        totalSavesLabel = Label(container, font=("ITC Novarese Std Medium", 30), text=f" • Atajadas: {keeperList[i][1]}", bg="#14223E", fg="#6594C0")
        totalSavesLabel.place(x=320, y=130)

        totalFailedLabel = Label(container, font=("ITC Novarese Std Medium", 30), text=f" • Atajadas fallidas: {keeperList[i][2]}", bg="#14223E", fg="#6594C0")
        totalFailedLabel.place(x=320, y=230)


def testMenu(window_width, window_height):
    global threadPicoRead

    root.title("Prueba de modulos")

    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    container.pack()

    stimulusLabel = Label(container, text="Escriba un estimulo", font=("Champions", 35), background="#14223E", fg="#FFFFFF")
    stimulusLabel.place(x=410, y=150)

    stimulus = StringVar()
    entryStimulus = Entry(container, textvariable=stimulus, font=("Champions", 35)).place(x=350, y=250)

    sendBtn = Button(container, text='ENVIAR', font=("Champions", 35), command=lambda:[sendToPico(stimulus.get())])
    sendBtn.place(x=500, y=350)

    sendBtn = Button(container, text='?', font=("Champions", 35), command=lambda:[threadPicoRead.start()])
    sendBtn.place(x=500, y=450)

    backBtn = Button(root, font=("Champions", 35), text="VOLVER", bg="#3562A6", fg="#FFFFFF",
                 command=lambda: [container.destroy(), mainMenu(window_width, window_height, Logo)])
    backBtn.place(x=1000, y=900)

# Menú configuración inicial
def initConfig(window_width, window_height):

    global logoMCI, logoRMA

    root.title("Configuración inicial")

    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    container.pack()

    container.create_image(600, 500, image=Stars)


    configTitle = Label(container, font=("Champions", 40), text="CONFIGURACIÓN INICIAL", bg="#14223E", fg="#FFFFFF")
    configTitle.place(x=30, y=30)

    pickTitle = Label(container, font=("ITC Novarese Std Medium", 30), text="ESCOJA DOS EQUIPOS", bg="#14223E", fg="#FFFFFF")
    pickTitle.place(x=100, y=250)

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
    decidePickAPlayer("Local")


def decidePickAPlayer(mode):
    global local, visiting, visitingPicking, wGonnaWin
    if mode == "Local":
        if local == "Manchester City":
            wGonnaWin = "Manchester City"
            pickAPlayerMCI()
        elif local == "Real Madrid":
            wGonnaWin = "Real Madrid"
            pickAPlayerRMA()
        elif local == "Barcelona FC":
            wGonnaWin = "Barcelona FC"
            pickAPlayerBAR()
    else:
        if visitingPicking:
            visitingPicking = False
            if visiting == "Manchester City":
                pickAPlayerMCI()
            elif visiting == "Real Madrid":
                pickAPlayerRMA()
            elif visiting == "Barcelona FC":
                pickAPlayerBAR()
        else:
            teamDraw()


def teamDraw():
    global coinFlipFrames, threadCoinFlipAnim
    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    container.pack()

    drawlist = [local, visiting]

    heads = random.choice(drawlist)
    del drawlist[drawlist.index(heads)]
    tails = drawlist[0]

    headsImg = iconAux(heads, tails, "heads")
    tailsImg = iconAux(heads, tails, "tails")

    drawTitle = Label(container, font=("Champions", 40), text="SORTEO LOCAL Y VISITANTE", bg="#14223E", fg="#FFFFFF")
    drawTitle.place(x=280, y=30)

    headTitle = Label(container, font=("ITC Novarese Std Ultra", 40), text="CARA", bg="#14223E", fg="#FFFFFF")
    headTitle.place(x=200, y=200)

    container.create_image(280, 450, image=headsImg)

    tailsTitle = Label(container, font=("ITC Novarese Std Ultra", 40), text="CRUZ", bg="#14223E", fg="#FFFFFF")
    tailsTitle.place(x=850, y=200)

    container.create_image(930, 450, image=tailsImg)

    coin = container.create_image(609, 450, image=coinFlipFrames[0])

    threadCoinFlipAnim = threading.Thread(target=coinFlipAnim, args=(coin, container, heads, tails))

    startButton = Button(container, text="INICIAR", font=("Champions", 40), command=lambda :[threadCoinFlipAnim.start(), startButton.destroy()])
    startButton.place(x=500, y=700)


def iconAux(heads, tails, mode):
    if mode == "heads":
        if heads == "Manchester City":
            headsImg = logoMCI
            return headsImg
        if heads == "Real Madrid":
            headsImg = logoRMA
            return headsImg
        if heads == "Barcelona FC":
            headsImg = logoBAR
            return headsImg
    else:
        if tails == "Manchester City":
            tailsImg = logoMCI
            return tailsImg
        if tails == "Real Madrid":
            tailsImg = logoRMA
            return tailsImg
        if tails == "Barcelona FC":
            tailsImg = logoBAR
            return tailsImg


def coinFlipAnim(coin, container, heads, tails):
    global coinFlipFrames, wGonnaWin
    loops = random.randint(2, 5)
    e = 0
    if wGonnaWin == heads:
        while e != loops:
            print(e)
            for i in range(len(coinFlipFrames)):
                container.itemconfig(coin, image=coinFlipFrames[i])
                time.sleep(0.1)
            e = e+1
        container.itemconfig(coin, image=coinFlipFrames[0])
        for i in range(1, 7):
            container.itemconfig(coin, image=coinFlipFrames[i])
            time.sleep(0.1)

    elif wGonnaWin == tails:
        while e != loops:
            print(e)
            for i in range(len(coinFlipFrames)):
                container.itemconfig(coin, image=coinFlipFrames[i])
                time.sleep(0.1)
            e = e+1
        container.itemconfig(coin, image=coinFlipFrames[0])

    time.sleep(0.5)

    winnerL = Label(container, text=f"¡El {wGonnaWin} será el local del partido!", width=40, font=("Champions", 40), fg="#FFFFFF", bg="#14223E", anchor="n")
    winnerL.place(x=60, y=700)

    time.sleep(1.5)

    timer = StringVar()
    timer.set("Inciando en 3 segundos")

    startingIn = Label(container, textvariable=timer, font=("Champions", 40), fg="#3562A6", bg="#14223E")
    startingIn.place(x=320, y=800)

    for i in range(3, -1, -1):
        timer.set(f"Iniciando en {i} segundos")
        time.sleep(1)

    container.destroy()
    startGame("Local")


def pickAPlayerMCI():
    global jugadoresImgs, playerNum
    def pickAKeeperMCI():
        container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#A6C8EA",
                           highlightbackground="#A6C8EA")
        container.pack()

        keepersList = ["Ederson Morae", "Scott Carson"]

        listajugadores = os.listdir("Manchester City/porteros-MCI")
        jugadoresImgs = []

        for i in listajugadores:
            id = Image.open(f"Manchester City/porteros-MCI/{i}")
            jugadoresImgs.append(ImageTk.PhotoImage(id))

        nav = Canvas(container, width=1200, height=300)
        nav.place(x=0, y=0)

        nav.create_image(150, 150, image=logoMCI)

        teamName = Label(nav, font=("ITC Novarese Std Ultra", 45), text="ESCOGE UN ARQUERO", fg="#002A5A")
        teamName.place(x=370, y=120)

        keeperCanvas = Canvas(container, width=400, height=400)
        keeperCanvas.place(x=410, y=400)

        keeperL = StringVar()
        keeperL.set("Ederson Morae")

        player = keeperCanvas.create_image(200, 220, image=jugadoresImgs[0])

        keeperName = Label(container, font=("Champions", 40), width=20, height=1, textvariable=keeperL, fg="#002A5A",
                            bg="#A6C8EA", anchor="n")
        keeperName.place(x=340, y=330)

        nextBtn = Button(container, font=("Champions", 40), text=">>>", bg="#002A5A", fg="#FFFFFF", command=lambda: [
            pickAKeeperAux(playerNum, keeperCanvas, "next", player, keeperL, keepersList, jugadoresImgs,
                           "Manchester City")])
        nextBtn.place(x=1000, y=850)

        previousBtn = Button(container, font=("Champions", 40), text="<<<", bg="#002A5A", fg="#FFFFFF",
                             command=lambda: [
                                 pickAKeeperAux(playerNum, keeperCanvas, "previous", player, keeperL, keepersList,
                                                jugadoresImgs, "Manchester City")])
        previousBtn.place(x=80, y=850)

        selectBtn = Button(container, font=("Champions", 40), text="SELECCIONAR", bg="#002A5A", fg="#FFFFFF",
                           command=lambda: [
                               pickAKeeperAux(playerNum, keeperCanvas, "choose", player, keeperL, keepersList,
                                              jugadoresImgs, "Manchester City"), container.destroy(), decidePickAPlayer("Visiting")])
        selectBtn.place(x=440, y=850)



    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#A6C8EA", highlightbackground="#A6C8EA")
    container.pack()

    strikersList = ["Erling Haaland", "Julián Alvarez", "K. De Bruyne", "Phil Foden"]

    listajugadores = os.listdir("Manchester City/jugadores-MCI")
    jugadoresImgs = []

    for i in listajugadores:
        id = Image.open(f"Manchester City/jugadores-MCI/{i}")
        jugadoresImgs.append(ImageTk.PhotoImage(id))

    #playerNum = 0

    nav = Canvas(container, width=1200, height=300)
    nav.place(x=0, y=0)

    nav.create_image(150, 150, image=logoMCI)

    teamName = Label(nav, font=("ITC Novarese Std Ultra", 45), text="ESCOGE UN ARTILLERO", fg="#002A5A")
    teamName.place(x=370, y=120)

    strikerCanvas = Canvas(container, width=400, height=400)
    strikerCanvas.place(x=410, y=400)

    strikerL = StringVar()
    strikerL.set("Erling Haaland")

    player = strikerCanvas.create_image(200, 220, image=jugadoresImgs[0])

    strikerName = Label(container, font=("Champions", 40), width=20, height=1, textvariable=strikerL, fg="#002A5A", bg="#A6C8EA", anchor="n")
    strikerName.place(x=340, y=330)

    nextBtn = Button(container, font=("Champions", 40), text=">>>", bg="#002A5A", fg="#FFFFFF", command=lambda:[pickAPlayerAux(playerNum, strikerCanvas, "next", player, strikerL,strikersList,jugadoresImgs, "Manchester City")])
    nextBtn.place(x=1000, y=850)

    previousBtn = Button(container, font=("Champions", 40), text="<<<", bg="#002A5A", fg="#FFFFFF", command=lambda:[pickAPlayerAux(playerNum, strikerCanvas, "previous", player, strikerL, strikersList, jugadoresImgs, "Manchester City")])
    previousBtn.place(x=80, y=850)

    selectBtn = Button(container, font=("Champions", 40), text="SELECCIONAR", bg="#002A5A", fg="#FFFFFF", command=lambda:[pickAPlayerAux(playerNum, strikerCanvas, "choose", player, strikerL, strikersList, jugadoresImgs, "Manchester City"), container.destroy(), pickAKeeperMCI()])
    selectBtn.place(x=440, y=850)


def pickAPlayerRMA():

    def pickAKeeperRMA():
        container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#FFFFFF",
                           highlightbackground="#A6C8EA")
        container.pack()

        keepersList = ["Andriy Lunin", "Thibaut Courtois"]

        listajugadores = os.listdir("Real Madrid/porteros-RMA")
        jugadoresImgs = []

        for i in listajugadores:
            id = Image.open(f"Real Madrid/porteros-RMA/{i}")
            jugadoresImgs.append(ImageTk.PhotoImage(id))

        nav = Canvas(container, width=1200, height=300, bg="#FEBE10", highlightbackground="#FEBE10")
        nav.place(x=0, y=0)

        nav.create_image(150, 150, image=logoRMA)

        teamName = Label(nav, font=("ITC Novarese Std Ultra", 45), text="ESCOGE UN ARQUERO", fg="#FFFFFF",
                         bg="#FEBE10")
        teamName.place(x=340, y=120)

        keeperCanvas = Canvas(container, width=400, height=400)
        keeperCanvas.place(x=410, y=400)

        keeperL = StringVar()
        keeperL.set("Andriy Lunin")

        player = keeperCanvas.create_image(200, 220, image=jugadoresImgs[0])

        strikerName = Label(container, font=("Champions", 40), width=20, height=1, textvariable=keeperL, fg="#000000",
                            bg="#FFFFFF", anchor="n")
        strikerName.place(x=340, y=330)

        nextBtn = Button(container, font=("Champions", 40), text=">>>", bg="#004996", fg="#FFFFFF", command=lambda: [
            pickAKeeperAux(playerNum, keeperCanvas, "next", player, keeperL, keepersList, jugadoresImgs,
                           "Manchester City")])
        nextBtn.place(x=1000, y=850)

        previousBtn = Button(container, font=("Champions", 40), text="<<<", bg="#004996", fg="#FFFFFF",
                             command=lambda: [
                                 pickAKeeperAux(playerNum, keeperCanvas, "previous", player, keeperL, keepersList,
                                                jugadoresImgs, "Manchester City")])
        previousBtn.place(x=80, y=850)

        selectBtn = Button(container, font=("Champions", 40), text="SELECCIONAR", bg="#004996", fg="#FFFFFF",
                           command=lambda: [
                               pickAKeeperAux(playerNum, keeperCanvas, "choose", player, keeperL, keepersList,
                                              jugadoresImgs, "Real Madrid"), container.destroy(), decidePickAPlayer("Visiting")])
        selectBtn.place(x=440, y=850)

    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#FFFFFF", highlightbackground="#FFFFFF")
    container.pack()

    strikersList = ["Jude Bellingham", "Luka Modrić", "Rodrygo Silva", "Vinicius Jr"]

    listajugadores = os.listdir("Real Madrid/jugadores-RMA")
    jugadoresImgs = []

    for i in listajugadores:
        id = Image.open(f"Real Madrid/jugadores-RMA/{i}")
        jugadoresImgs.append(ImageTk.PhotoImage(id))

    #playerNum = 0

    nav = Canvas(container, width=1200, height=300, bg="#FEBE10", highlightbackground="#FEBE10")
    nav.place(x=0, y=0)

    nav.create_image(150, 150, image=logoRMA)

    teamName = Label(nav, font=("ITC Novarese Std Ultra", 45), text="ESCOGE UN ARTILLERO", fg="#FFFFFF", bg="#FEBE10")
    teamName.place(x=340, y=120)

    strikerCanvas = Canvas(container, width=400, height=400)
    strikerCanvas.place(x=410, y=400)

    strikerL = StringVar()
    strikerL.set("Jude Bellingham")

    player = strikerCanvas.create_image(200, 220, image=jugadoresImgs[0])

    strikerName = Label(container, font=("Champions", 40), width=20, height=1, textvariable=strikerL, fg="#000000", bg="#FFFFFF", anchor="n")
    strikerName.place(x=340, y=330)

    nextBtn = Button(container, font=("Champions", 40), text=">>>", bg="#004996", fg="#FFFFFF", command=lambda:[pickAPlayerAux(playerNum, strikerCanvas, "next", player, strikerL,strikersList,jugadoresImgs, "Real Madrid")])
    nextBtn.place(x=1000, y=850)

    previousBtn = Button(container, font=("Champions", 40), text="<<<", bg="#004996", fg="#FFFFFF", command=lambda:[pickAPlayerAux(playerNum, strikerCanvas, "previous", player, strikerL, strikersList, jugadoresImgs, "Real Madrid")])
    previousBtn.place(x=80, y=850)

    selectBtn = Button(container, font=("Champions", 40), text="SELECCIONAR", bg="#004996", fg="#FFFFFF", command=lambda:[pickAPlayerAux(playerNum, strikerCanvas, "choose", player, strikerL, strikersList, jugadoresImgs, "Real Madrid"), container.destroy(), pickAKeeperRMA()])
    selectBtn.place(x=440, y=850)


def pickAPlayerBAR():
    def pickAKeeperBAR():
        container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#FFFFFF",
                           highlightbackground="#A6C8EA")
        container.pack()

        keepersList = ["Iñaki Peña", "Marc-André ter Stegen"]

        listajugadores = os.listdir("Barcelona FC/porteros-BAR")
        jugadoresImgs = []

        for i in listajugadores:
            id = Image.open(f"Barcelona FC/porteros-BAR/{i}")
            jugadoresImgs.append(ImageTk.PhotoImage(id))

        nav = Canvas(container, width=1200, height=300, bg="#A50044", highlightbackground="#A50044")
        nav.place(x=0, y=0)

        nav.create_image(150, 150, image=logoBAR)

        teamName = Label(nav, font=("ITC Novarese Std Ultra", 45), text="ESCOGE UN ARQUERO", fg="#FFFFFF",
                         bg="#A50044")
        teamName.place(x=340, y=120)

        keeperCanvas = Canvas(container, width=400, height=400)
        keeperCanvas.place(x=410, y=400)

        keeperL = StringVar()
        keeperL.set("Andriy Lunin")

        player = keeperCanvas.create_image(200, 220, image=jugadoresImgs[0])

        strikerName = Label(container, font=("Champions", 40), width=20, height=1, textvariable=keeperL, fg="#000000",
                            bg="#FFFFFF", anchor="n")
        strikerName.place(x=340, y=330)

        nextBtn = Button(container, font=("Champions", 40), text=">>>", bg="#A50044", fg="#FFFFFF", command=lambda: [
            pickAKeeperAux(playerNum, keeperCanvas, "next", player, keeperL, keepersList, jugadoresImgs,
                           "Barcelona FC")])
        nextBtn.place(x=1000, y=850)

        previousBtn = Button(container, font=("Champions", 40), text="<<<", bg="#A50044", fg="#FFFFFF",
                             command=lambda: [
                                 pickAKeeperAux(playerNum, keeperCanvas, "previous", player, keeperL, keepersList,
                                                jugadoresImgs, "Barcelona FC")])
        previousBtn.place(x=80, y=850)

        selectBtn = Button(container, font=("Champions", 40), text="SELECCIONAR", bg="#A50044", fg="#FFFFFF",
                           command=lambda: [
                               pickAKeeperAux(playerNum, keeperCanvas, "choose", player, keeperL, keepersList,
                                              jugadoresImgs, "Barcelona FC"), container.destroy(), decidePickAPlayer("Visiting")])
        selectBtn.place(x=440, y=850)

    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#FFFFFF", highlightbackground="#FFFFFF")
    container.pack()

    strikersList = ["Ilkay Gündogan", "João Cancelo", "Robert Lewandowski", "Pedri"]

    listajugadores = os.listdir("Barcelona FC/jugadores-BAR")
    jugadoresImgs = []

    for i in listajugadores:
        id = Image.open(f"Barcelona FC/jugadores-BAR/{i}")
        jugadoresImgs.append(ImageTk.PhotoImage(id))

    #playerNum = 0

    nav = Canvas(container, width=1200, height=300, bg="#A50044", highlightbackground="#A50044")
    nav.place(x=0, y=0)

    nav.create_image(150, 150, image=logoBAR)

    teamName = Label(nav, font=("ITC Novarese Std Ultra", 45), text="ESCOGE UN ARTILLERO", fg="#FFFFFF", bg="#A50044")
    teamName.place(x=340, y=120)

    strikerCanvas = Canvas(container, width=400, height=400)
    strikerCanvas.place(x=410, y=400)

    strikerL = StringVar()
    strikerL.set("Ilkay Gündogan")

    player = strikerCanvas.create_image(200, 220, image=jugadoresImgs[0])

    strikerName = Label(container, font=("Champions", 40), width=20, height=1, textvariable=strikerL, fg="#000000", bg="#FFFFFF", anchor="n")
    strikerName.place(x=340, y=330)

    nextBtn = Button(container, font=("Champions", 40), text=">>>", bg="#A50044", fg="#FFFFFF", command=lambda:[pickAPlayerAux(playerNum, strikerCanvas, "next", player, strikerL,strikersList,jugadoresImgs, "Barcelona FC")])
    nextBtn.place(x=1000, y=850)

    previousBtn = Button(container, font=("Champions", 40), text="<<<", bg="#A50044", fg="#FFFFFF", command=lambda:[pickAPlayerAux(playerNum, strikerCanvas, "previous", player, strikerL, strikersList, jugadoresImgs, "Barcelona FC")])
    previousBtn.place(x=80, y=850)

    selectBtn = Button(container, font=("Champions", 40), text="SELECCIONAR", bg="#A50044", fg="#FFFFFF", command=lambda:[pickAPlayerAux(playerNum, strikerCanvas, "choose", player, strikerL, strikersList, jugadoresImgs, "Barcelona FC"), container.destroy(), pickAKeeperBAR()])
    selectBtn.place(x=440, y=850)

def pickAPlayerAux(player_num, strikerCanvas, mode, player, strikerL, strikersList, jugadoresImgs, team):
    global playerNum, localStriker, visitingStriker, localBench, visitingBench
    if mode == "next":
        playerNum += 1
        if playerNum == 4:
            playerNum = 0
            strikerL.set(f"{strikersList[0]}")
        if playerNum == 0:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[0])
            strikerL.set(f"{strikersList[0]}")
        if playerNum == 1:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[1])
            strikerL.set(f"{strikersList[1]}")
        if playerNum == 2:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[2])
            strikerL.set(f"{strikersList[2]}")
        if playerNum == 3:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[3])
            strikerL.set(f"{strikersList[3]}")
    if mode == "previous":
        playerNum = playerNum - 1
        if playerNum == -1:
            strikerL.set(f"{strikersList[3]}")
            playerNum = 3
        if playerNum == 0:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[0])
            strikerL.set(f"{strikersList[0]}")
        if playerNum == 1:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[1])
            strikerL.set(f"{strikersList[1]}")
        if playerNum == 2:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[2])
            strikerL.set(f"{strikersList[2]}")
        if playerNum == 3:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[3])
            strikerL.set(f"{strikersList[3]}")
    if mode == "choose":
        if team == local:
            localStriker = f"{strikersList[playerNum]}"
            del strikersList[playerNum]
            localBench = strikersList
            print(localBench)
        else:
            visitingStriker = f"{strikersList[playerNum]}"
            del strikersList[playerNum]
            visitingBench = strikersList
        playerNum = 0


def pickAKeeperAux(player_num, strikerCanvas, mode, player, strikerL, keepersList, jugadoresImgs, team):
    global playerNum, localKeeper, visitingKeeper
    if mode == "next":
        playerNum += 1
        if playerNum == 2:
            playerNum = 0
            strikerL.set(f"{keepersList[0]}")
        if playerNum == 0:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[0])
            strikerL.set(f"{keepersList[0]}")
        if playerNum == 1:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[1])
            strikerL.set(f"{keepersList[1]}")
    if mode == "previous":
        playerNum = playerNum - 1
        if playerNum == -1:
            strikerL.set(f"{keepersList[1]}")
            playerNum = 1
        if playerNum == 0:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[0])
            strikerL.set(f"{keepersList[0]}")
        if playerNum == 1:
            strikerCanvas.itemconfig(player, image=jugadoresImgs[1])
            strikerL.set(f"{keepersList[1]}")
    if mode == "choose":
        if team == local:
            localKeeper = f"{keepersList[playerNum]}"
        else:
            visitingKeeper = f"{keepersList[playerNum]}"


def startGame(mode):
    global scrRedon, scrLcl, localStriker, localBench, localPlayed, visitingPlayed, visitingStriker, visitingBench, round, datos
    datos.clear()
    root.title(f"{local} vs {visiting}")

    pygame.mixer.music.fadeout(4000)

    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E",
                       highlightbackground="#14223E")
    container.pack()

    localL, visitingL = getLogo()

    container.create_image(430, 200, image=scrLcl)

    container.create_image(200, 200, image=scrRedon)

    container.create_image(200, 200, image=localL)

    container.create_image(770, 200, image=scrLcl)

    container.create_image(1000, 200, image=scrRedon)

    container.create_image(1000, 200, image=visitingL)

    lblScore = Label(container, textvariable=localScore, font=("Champions", 70), background="#2150ff", foreground="#FFFFFF").place(x=415,y=150)

    lbvScore = Label(container, textvariable=visitingScore, font=("Champions", 70), background="#2150ff", foreground="#FFFFFF").place(x=745,y=150)

    roundL = Label(container, text=f"Ronda {round}", font=("Champions", 45), background="#14223E", foreground="#FFFFFF").place(x=500,y=350)

    if mode == "Local":
        sendToPico("Lled")
        timeto = Label(container, text=f"Es el turno del {local}.", font=("Champions", 40), width=40, background="#14223E", anchor="n",
                         foreground="#FFFFFF")
        timeto.place(x=60, y=600)

        pygame.mixer.Sound.play(cheersSF)
        time.sleep(2)

        timeto["text"] = f"{localStriker} se prepara para tirar"

        pygame.mixer.Sound.play(initPitido)

        time.sleep(4)

        sendToPico("read")

        pygame.mixer.Sound.fadeout(cheersSF, 2)

        pygame.mixer.Sound.play(initPitido)

        timeto["text"] = f"¡TIRA AL ARCO!"

        simulateStrike = [random.choice(["P1","P2","P3","P4","P5","P6"])]

        ghostKeeper()

        countdown = StringVar()

        countdown.set("3s")

        timeLeft = Label(container, textvariable=countdown, font=("Champions", 40), fg="#3562A6", bg="#14223E")
        timeLeft.place(x=580, y=700)

        for i in range(3, -1, -1):
            countdown.set(f"{i}s")
            time.sleep(1)

        datos_lista = list(datos)
        print(datos_lista)
        
        if handleGoal(datos_lista):
            #sendToPico("goalA")
            print(localStriker)
            if int(localScore.get()) < 7:
                localScore.set(f"{int(localScore.get())+1}")
            pygame.mixer.Sound.play(goalSF)
            timeto["text"] = "G"
            for i in range(0, 15):
                timeto["text"] += "O"
                time.sleep(0.5)
                if i == 14:
                    timeto["text"] += "L"

            with open("teams-data-base.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            for team in data["Teams"]:
                if team["Team"] == local:
                    for player in team["Strikers"]:
                        if player["Name"] == localStriker:
                            player["Goals"] = str(int(player["Goals"]) + 1)
                if team["Team"] == visiting:
                    for keeper in team["Keepers"]:
                        if keeper["Name"] == visitingKeeper:
                            keeper["Failed"] = str(int(keeper["Failed"]) + 1)

            with open("teams-data-base.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=1)

        if not handleGoal(datos_lista):
            timeto["text"] = f"¡Tapó {visitingKeeper}!"

            with open("teams-data-base.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            for team in data["Teams"]:
                if team["Team"] == local:
                    for player in team["Strikers"]:
                        if player["Name"] == localStriker:
                            player["Failed"] = str(int(player["Failed"]) + 1)
                if team["Team"] == visiting:
                    for keeper in team["Keepers"]:
                        if keeper["Name"] == visitingKeeper:
                            keeper["Saves"] = str(int(keeper["Saves"]) + 1)

            with open("teams-data-base.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=1)

            pygame.mixer.Sound.play(abucheosSF)
            time.sleep(3)
            pygame.mixer.Sound.fadeout(abucheosSF, 2)

        localBench.append(localStriker)
        localStriker = localBench[0]
        del localBench [0]

        print(datos)

        localPlayed = True
        time.sleep(1)

        varRandom = random.randint(0, 1)

        if varRandom == 1:
            timeLeft.destroy()
            varEvent(timeto, container, localScore)
            print("VAR")
        else:
            container.destroy()
            roundHandler()

    if mode == "Visiting":
        sendToPico("Vled")
        timeto = Label(container, text=f"Es el turno del {visiting}.", font=("Champions", 40), width=40, background="#14223E", anchor="n",
                         foreground="#FFFFFF")
        timeto.place(x=60, y=600)

        pygame.mixer.Sound.play(cheersSF)
        time.sleep(2)

        timeto["text"] = f"{visitingStriker} se prepara para tirar"

        pygame.mixer.Sound.play(initPitido)

        time.sleep(4)

        sendToPico("read")

        pygame.mixer.Sound.fadeout(cheersSF, 2)

        pygame.mixer.Sound.play(initPitido)

        timeto["text"] = f"¡TIRA AL ARCO!"

        simulateStrike = [random.choice(["P1","P2","P3","P4","P5","P6"])]

        ghostKeeper()

        countdown = StringVar()

        countdown.set("3s")

        timeLeft = Label(container, textvariable=countdown, font=("Champions", 40), fg="#3562A6", bg="#14223E")
        timeLeft.place(x=580, y=700)

        for i in range(3, -1, -1):
            countdown.set(f"{i}s")
            time.sleep(1)

        datos_lista = list(datos)
        print(datos_lista)

        if handleGoal(datos_lista):
            print(visitingStriker)
            #sendToPico("goalA")
            if int(visitingScore.get()) < 7:
                visitingScore.set(f"{int(visitingScore.get())+1}")
            pygame.mixer.Sound.play(goalSF)
            timeto["text"] = "G"
            for i in range(0, 15):
                timeto["text"] += "O"
                time.sleep(0.5)
                if i == 14:
                    timeto["text"] += "L"

            with open("teams-data-base.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            for team in data["Teams"]:
                if team["Team"] == visiting:
                    for player in team["Strikers"]:
                        if player["Name"] == visitingStriker:
                            player["Goals"] = str(int(player["Goals"]) + 1)
                if team["Team"] == local:
                    for keeper in team["Keepers"]:
                        if keeper["Name"] == localStriker:
                            keeper["Failed"] = str(int(keeper["Failed"]) + 1)

            with open("teams-data-base.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=1)

        elif not handleGoal(datos_lista):
            timeto["text"] = f"¡Tapó {localKeeper}!"

            with open("teams-data-base.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            for team in data["Teams"]:
                if team["Team"] == visiting:
                    for player in team["Strikers"]:
                        if player["Name"] == visitingStriker:
                            player["Failed"] = str(int(player["Failed"]) + 1)
                if team["Team"] == local:
                    for keeper in team["Keepers"]:
                        if keeper["Name"] == localKeeper:
                            keeper["Saves"] = str(int(keeper["Saves"]) + 1)

            with open("teams-data-base.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=1)

            pygame.mixer.Sound.play(abucheosSF)
            time.sleep(3)
            pygame.mixer.Sound.fadeout(abucheosSF, 2)

        visitingBench.append(visitingStriker)
        visitingStriker = visitingBench[0]
        del visitingBench[0]

        print(datos)

        visitingPlayed = True
        time.sleep(1)

        varRandom = random.randint(0, 1)

        if varRandom == 1:
            timeLeft.destroy()
            varEvent(timeto, container, visitingScore)
        else:
            container.destroy()
            roundHandler()

def varEvent(timeto, container, score):
    global varSF
    print("VAR")
    pygame.mixer.Sound.play(varSF)
    timeto["text"] = "¡EL VAR DETECTÓ UNA INFRACCIÓN!"
    time.sleep(3)
    timeto["text"] = "Se decidirá un marcador adecuado..."
    time.sleep(2)

    ms = 0.05

    pygame.mixer.Sound.play(spinSF)

    newScore = circularSubtract(int(score.get()))
    print(newScore)

    binaryScore = "1" + str(binaryConverter(int(score.get())))
    print(binaryScore)

    for i in range(0, 60):
        randomNum = random.randint(0, 7)
        score.set(f"{randomNum}")
        ms += 0.003
        time.sleep(ms)

    sendToPico(binaryScore)

    score.set(f"{newScore}")

    time.sleep(3)

    container.destroy()

    roundHandler()

def circularSubtract(a, n=8):
    return (a - 3 + n) % n

def binaryConverter(n):
    if 0 <= n <= 7:
        return bin(n)[2:].zfill(3)
    else:
        raise ValueError("El número debe estar entre 0 y 7")

def getLogo():
    global local, visiting

    localL = None
    visitingL = None

    if local == "Manchester City":
        localL = logoMCI_est
    if local == "Real Madrid":
        localL = logoRMA_est
    if local == "Barcelona FC":
        localL = logoBAR_est
    if visiting == "Manchester City":
        visitingL = logoMCI_est
    if visiting == "Real Madrid":
        visitingL = logoRMA_est
    if visiting == "Barcelona FC":
        visitingL = logoBAR_est
    return localL, visitingL


def ghostKeeper():
    global ghostKeeperPos
    AN1 = [["P1", "P2"], ["P3","P4"], ["P5","P6"]]
    AN2 = [["P1","P2","P3"], ["P4", "P5", "P6"]]

    method = random.choice(["AN1", "AN2"])

    if method == "AN1":
        ghostKeeperPos = random.choice(AN1)

    else:
        ghostKeeperPos = random.choice(AN2)

    print(ghostKeeperPos)


def handleGoal(touchedContacts):
    print(touchedContacts)
    global ghostKeeperPos
    if touchedContacts == []:
        return False
    for i in range(len(ghostKeeperPos)):
        for j in range(len(touchedContacts)):
            print(ghostKeeperPos[i], touchedContacts[j])
            if ghostKeeperPos[i] == touchedContacts[j]:
                return False
    return True


def roundHandler():
    global localPlayed, visitingPlayed, round, datos
    if localPlayed and not visitingPlayed:
        startGame("Visiting")
    elif localPlayed and visitingPlayed:
        round = round + 1
        if round >= 6:
            if not(localScore.get() == visitingScore.get()):
                if int(localScore.get()) > int(visitingScore.get()):
                    return endGame(local)
                else:
                    return endGame(visiting)
        localPlayed = False
        visitingPlayed = False
        startGame("Local")


def endGame(nameW):
    pygame.mixer.music.play(-1)
    logoW = None
    if nameW == "Manchester City":
        logoW = logoMCIW
    elif nameW == "Real Madrid":
        logoW = logoRMAW
    elif nameW == "Barcelona FC":
        logoW = logoBARW

    container = Canvas(root, width=f"{window_width}", height=f"{window_height}", background="#14223E", highlightbackground="#14223E")
    container.pack()

    container.create_image(600, 300, image=logoW)

    wLabel = Label(container, text=f"{nameW} ha ganado el partido.", font=("Champions", 40), bg="#14223E", foreground="#FFFFFF", width=40, anchor="n")
    wLabel.place(x=50, y=500)

    backBtn = Button(container, text="VOLVER AL MENÚ", font=("Champions", 40), command=lambda:[container.destroy(), mainMenu(window_width, window_height, Logo)])
    backBtn.place(x=390, y=700)

    restart()


def restart():
    global datos, firstTeam, secondTeam, round, local, localStriker, localKeeper, localBench, localScore, localPlayed, visiting, visitingStriker, visitingBench, visitingKeeper, visitingScore, visitingPlayed, visitingPicking, ghostKeeperPos, playerNum, wGonnaWin
    datos = set()

    firstTeam = None
    secondTeam = None

    round = 1

    local = None
    localStriker = None
    localKeeper = None
    localBench = []
    localScore = StringVar()
    localScore.set("0")
    localPlayed = False

    visiting = None
    visitingStriker = None
    visitingKeeper = None
    visitingBench = []
    visitingScore = StringVar()
    visitingScore.set("0")
    visitingPlayed = False

    visitingPicking = True

    ghostKeeperPos = None

    playerNum = 0

    wGonnaWin = None


def sendToPico(message):
    #btn["state"] = "disabled"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_raspberry, 8080))
    #s.listen(1)
    #conexion, direccion = s.accept()
    s.sendall(message.encode())
    s.close()
    print("Mensaje enviado.")
    #readFromPico()


def readFromPico():
    while True:
        try:
            readFromPicoAux()
        except Exception as e:
            print(e)


def readFromPicoAux():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_server, server_port))
    s.listen(1)
    conexion, direccion = s.accept()
    print("Conectado con:", direccion)

    while True:
        respuesta = conexion.recv(1024).decode()
        if not respuesta:
            break
        print(respuesta)
        datos.add(respuesta)
        print(datos)
        time.sleep(0.1)

    conexion.close()

root = Tk()

window_width = 1200
window_height = 1000

root.geometry(f"{window_width}x{window_height}")
root.resizable(width=False, height=False)
root.config(background="#14223E")

pygame.mixer.init()

initPitido = pygame.mixer.Sound("sound_effects/silbato.mp3")
cheersSF = pygame.mixer.Sound("sound_effects/cheers.mp3")
goalSF = pygame.mixer.Sound("sound_effects/goal.mp3")
abucheosSF = pygame.mixer.Sound("sound_effects/abucheos.mp3")
musicLoop = pygame.mixer.music.load("sound_effects/tema.mp3")
varSF = pygame.mixer.Sound("sound_effects/Interrupción  Efecto de sonido.mp3")
spinSF = pygame.mixer.Sound("sound_effects/spin.mp3")
pygame.mixer.music.play(-1)

# Imágenes de la interfaz

openLogo = Image.open("assets/logo.png")
Logo = ImageTk.PhotoImage(openLogo.resize((1000, 1000)))

openLogoTEC = Image.open("assets/logoTECBLANCO.png")
LogoTEC = ImageTk.PhotoImage(openLogoTEC)

openStars = Image.open("assets/stars.png")
Stars = ImageTk.PhotoImage(openStars)

logoMCIOp = Image.open("assets/LogoMCI.png")
logoMCI = ImageTk.PhotoImage(logoMCIOp.resize((250, 250)))
logoMCI_est = ImageTk.PhotoImage(logoMCIOp.resize((200, 200)))
logoMCIW = ImageTk.PhotoImage(logoMCIOp.resize((350, 350)))

logoRMAOp = Image.open("assets/LogoRMA.png")
logoRMA = ImageTk.PhotoImage(logoRMAOp.resize((200, 250)))
logoRMA_est = ImageTk.PhotoImage(logoRMAOp.resize((150, 200)))
logoRMAW = ImageTk.PhotoImage(logoRMAOp.resize((300, 350)))


logoBAROp = Image.open("assets/logoBAR.png")
logoBAR = ImageTk.PhotoImage(logoBAROp.resize((250, 250)))
logoBAR_est = ImageTk.PhotoImage(logoBAROp.resize((200, 200)))
logoBARW = ImageTk.PhotoImage(logoBAROp.resize((350, 350)))


scrRedonOp = Image.open("assets/SCORERedondo.png")
scrRedon = ImageTk.PhotoImage(scrRedonOp.resize((250, 250)))

scrLclOp = Image.open("assets/SCORELocal.png")
scrLcl = ImageTk.PhotoImage(scrLclOp.resize((250, 250)))


# Variables para el funcionamiento del juego

datos = set()

firstTeam = None
secondTeam = None

round = 1

local = None
localStriker = None
localKeeper = None
localBench = []
localScore = StringVar()
localScore.set("0")
localPlayed = False

visiting = None
visitingStriker = None
visitingKeeper = None
visitingBench = []
visitingScore = StringVar()
visitingScore.set("0")
visitingPlayed = False

visitingPicking = True

ghostKeeperPos = None

playerNum = 0

wGonnaWin = None

coinFlipFrames = []
coinFlipSprites = natsort.natsorted(os.listdir('coinflip'))

for i in coinFlipSprites:
    id = Image.open(f"coinflip/{i}")
    coinFlipFrames.append(ImageTk.PhotoImage(id))

totalGoals = StringVar()
totalSaves = StringVar()
totalFailed = StringVar()
topStriker = StringVar()
strikerList = []
keeperList = []

# Conexion con la Raspberry Pi Pico

ip_server = "0.0.0.0"
ip_raspberry = "192.168.0.4"
server_port = 50000
enabled = True

threadCoinFlipAnim = threading.Thread(target=coinFlipAnim)

threadPicoRead = threading.Thread(target=readFromPico)
threadPicoRead.start()

#threadPicoSend = threading.Thread(target=sendPico)
#threadPicoSend.start()

mainMenu(window_width, window_height, Logo)

root.mainloop()