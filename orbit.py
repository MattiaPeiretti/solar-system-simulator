import pygame
import time
import random
import numpy as np
import math
import tkinter as tk
import threading

from tkinter import *

zoomT = ""

# Funzioni


def accelerazioneX(x1, y1, x2, y2, g):
    deltaX = x2 - x1
    deltaY = y2 - y1
    if (deltaX < 0):
        sign = -1
    else:
        sign = 1

    distanzaAbs = distanza(x1, y1, x2, y2) * sign
    angolo = math.asin(deltaX / distanzaAbs)
    forza = g / math.pow(distanzaAbs, 2)

    return (forza * math.sin(angolo)) * sign


def accelerazioneY(x1, y1, x2, y2, g):
    deltaX = x2 - x1
    deltaY = y2 - y1
    if (deltaY < 0):
        sign = -1
    else:
        sign = 1
    distanzaAbs = distanza(x1, y1, x2, y2) * sign
    angolo = math.acos(deltaY / distanzaAbs)
    forza = g / math.pow(distanzaAbs, 2)

    return (forza * math.cos(angolo)) * sign


def distanza(x1, y1, x2, y2):
    distX = x1 - x2
    distY = y1 - y2

    distan = math.sqrt((distX*distX) + (distY*distY))
    return distan

# Control Panel


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.geometry("300x500")
        self.zoomTimothy = StringVar()
        self.gravityTimothy = StringVar()

        # zoom
        Label(self.root, text="Zoom Value:  ").grid(row=2, column=1)
        Entry(self.root, textvariable=self.zoomTimothy).grid(row=2, column=2)
        Button(self.root, text="Zoom +",
               command=self.increaseZoom).grid(row=3, column=1)
        Button(self.root, text="Zoom -",
               command=self.decreaseZoom).grid(row=3, column=2)

        # gravity
        Label(self.root, text="Gravity Value:  ").grid(row=4, column=1)
        Entry(self.root, textvariable=self.gravityTimothy).grid(row=4, column=2)

        Button(self.root, text="Reset Universe",
               command=inizia).grid(row=5, column=1)

        self.zoomTimothy.set(zoom)
        label = tk.Label(self.root, text="Hello World")
        # label.pack()

        self.root.mainloop()

    def increaseZoom(self):
        gameDisplay.fill((0, 0, 0))
        a = float(self.zoomTimothy.get())
        a = a + (a / 4)
        a = round(a, 4)
        self.zoomTimothy.set(a)
        return a

    def decreaseZoom(self):
        gameDisplay.fill((0, 0, 0))
        a = float(self.zoomTimothy.get())
        a = a - (a / 4)
        a = round(a, 4)
        self.zoomTimothy.set(a)
        return a

    def getZoom(self):
        tempZoom = self.zoomTimothy.get()
        if tempZoom != "":
            return self.zoomTimothy.get()
        else:
            return 0


bodys = list(range(100))


pygame.init()
#####################

font1 = pygame.font.SysFont("Segoe UI", 15)

speed = 0.5

gravityL = 8

bounce = False

zoom = 0.1

Nbodys = 20

running = True

activeBodies = Nbodys

###################


white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill((0, 0, 0))


def inizia():
    global running
    running = False


def inizz():
    gameDisplay.fill((0, 0, 0))
    for b in range(0, Nbodys):
        bodys[b] = {'objName': "body" + str(b),
                    'X': random.randint(-7899, 7899),
                    'Y': random.randint(-7899, 7899),
                    'oldX': 0,
                    'oldY': 0,
                    'diam': 0,
                    'speedX': random.randint(speed * -100, speed * 100) / 100,
                    'speedY': random.randint(speed * -100, speed * 100) / 100,
                    'gravity': random.randint(10, gravityL * 100) / 100,
                    'color': [random.randint(128, 255), random.randint(128, 255), random.randint(128, 255)],
                    'exists': True}
        bodys[b]['diam'] = bodys[b]['gravity'] * 2

    bodys[0]['objName'] = font1.render("The Sun", 1, (255, 255, 255))
    bodys[0]['diam'] = 15
    bodys[0]['gravity'] = gravityL * 1000
    bodys[0]['speedX'] = 0
    bodys[0]['speedY'] = 0


inizz()

inter = App()

while(True):

    if running == False:
        gameDisplay.fill((0, 0, 0))
        for b in range(0, Nbodys):
            bodys[b] = {'objName': "body",
                        'X': random.randint(-7899, 7899),
                        'Y': random.randint(-7899, 7899),
                        'oldX': 0,
                        'oldY': 0,
                        'diam': 0,
                        'speedX': random.randint(speed * -100, speed * 100) / 100,
                        'speedY': random.randint(speed * -100, speed * 100) / 100,
                        'gravity': random.randint(10, gravityL * 100) / 100,
                        'color': [random.randint(128, 255), random.randint(128, 255), random.randint(128, 255)],
                        'exists': True}
            bodys[b]['diam'] = bodys[b]['gravity'] * 2

        bodys[0]['objName'] = "The Sun"
        bodys[0]['diam'] = 15
        bodys[0]['gravity'] = gravityL * 1000
        bodys[0]['speedX'] = 0
        bodys[0]['speedY'] = 0

        running = True

    try:
        zoomT = float(inter.getZoom())
        if (zoomT != 0):
            zoom = zoomT
        # Calculation zoom percentages
        per = (float(inter.getZoom()) / 1) * 100
        per = round(per, 2)
        activeBLabel = font1.render(
            "Active Bodies: " + str(activeBodies) + "    Zoom:  " + str(per) + "%", 2, (255, 255, 255))
        gameDisplay.blit(activeBLabel, (10, 570))

    except:
        print("Mi sono incazzato")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break

    centerXX = bodys[0]['X']
    centerYY = bodys[0]['Y']

    for b in range(0, Nbodys):
        if bodys[b]['exists']:
            bodys[b]['oldX'] = bodys[b]['X']
            bodys[b]['oldY'] = bodys[b]['Y']
            for c in range(0, Nbodys):

                if bodys[c]['exists']:
                    if (b != c):
                        bodys[b]['speedX'] += accelerazioneX(bodys[b]['oldX'], bodys[b]['oldY'],
                                                             bodys[c]['oldX'], bodys[c]['oldY'], bodys[c]['gravity'])
                        bodys[b]['speedY'] += accelerazioneY(bodys[b]['oldX'], bodys[b]['oldY'],
                                                             bodys[c]['oldX'], bodys[c]['oldY'], bodys[c]['gravity'])
                        distBodys = distanza(
                            bodys[b]['oldX'], bodys[b]['oldY'], bodys[c]['oldX'], bodys[c]['oldY'])
                        if distBodys < bodys[b]['diam'] + bodys[c]['diam']:
                            activeBodies -= 1
                            if bodys[b]['gravity'] > bodys[c]['gravity']:
                                bodys[c]['exists'] = False
                                gravityRatio = bodys[b]['gravity'] / \
                                    bodys[c]['gravity']
                                bodys[b]['gravity'] += bodys[c]['gravity']
                                bodys[b]['speedX'] += bodys[c]['speedX'] / \
                                    gravityRatio
                                bodys[b]['speedY'] += bodys[c]['speedY'] / \
                                    gravityRatio
                                bodys[b]['diam'] = bodys[b]['gravity'] * 2
                            else:
                                bodys[b]['exists'] = False
                                gravityRatio = bodys[c]['gravity'] / \
                                    bodys[b]['gravity']
                                bodys[c]['gravity'] += bodys[b]['gravity']
                                bodys[c]['speedX'] += bodys[b]['speedX'] / \
                                    gravityRatio
                                bodys[c]['speedY'] += bodys[b]['speedY'] / \
                                    gravityRatio
                                bodys[c]['diam'] = bodys[c]['gravity'] * 2

            # print("speeds", bodys[b]['speedX'], bodys[b]['speedY'])
            bodys[b]['X'] = bodys[b]['X'] + bodys[b]['speedX']
            bodys[b]['Y'] = bodys[b]['Y'] + bodys[b]['speedY']

    # Drawing Bodys
        bodys[0]['diam'] = 15
        for b in range(0, Nbodys):
            if bodys[b]['exists']:
                pygame.draw.circle(gameDisplay, (bodys[b]['color']), (int(((bodys[b]['X'] - centerXX) * zoom) + 400), int(
                    ((bodys[b]['Y'] - centerYY)*zoom) + 300)), int(bodys[b]['diam']), int(bodys[b]['diam']))

                pygame.draw.line(gameDisplay, (255, 255, 255),
                                 (int(((bodys[b]['X'] - centerXX)*zoom) + 400),
                                  int(((bodys[b]['Y'] - centerYY)*zoom) + 300)),
                                 (int(((bodys[b]['X'] - centerXX)*zoom) + 420),
                                  int(((bodys[b]['Y'] - centerYY)*zoom) + 260)))

                sidA = (bodys[b]['X'] - bodys[b]['oldX'])
                sidB = (bodys[b]['Y'] - bodys[b]['oldY'])

                sidC = sidB / sidA
                sidC = sidC * -1

                pygame.draw.line(gameDisplay, (255, 255, 255),
                                 (bodys[b]['X'] * zoom, bodys[b]['Y'] * zoom),  (bodys[b]['speedX'] * 20 * zoom, bodys[b]['speedY']*20 * zoom))

                gameDisplay.blit(font1.render('{}{}'.format(bodys[b]['objName'], bodys[b]['speedX']), 2, (255, 255, 255)),
                                 (int(((bodys[b]['X'] - centerXX) * zoom) + 420),
                                  int(((bodys[b]['Y'] - centerYY) * zoom) + 240)))

    pygame.display.update()

    bodys[0]['diam'] = 15
    # Ereasing bodys
    for b in range(0, Nbodys):
        gameDisplay.fill((0, 0, 0))
        pygame.draw.circle(gameDisplay, (0, 0, 0), (int(((bodys[b]['oldX'] - centerXX) * zoom) + 400), int(
            ((bodys[b]['oldY'] - centerYY) * zoom) + 300)), int(bodys[b]['diam']+2), int(bodys[b]['diam']+2))
        pygame.draw.line(gameDisplay, (0, 0, 0),
                         (int(((bodys[b]['oldX'] - centerXX) * zoom) + 400),
                          int(((bodys[b]['oldY'] - centerYY) * zoom) + 300)),
                         (int(((bodys[b]['oldX'] - centerXX) * zoom) + 420),
                          int(((bodys[b]['oldY'] - centerYY) * zoom) + 260)), 3)
        pygame.draw.rect(gameDisplay, (0, 0, 0), pygame.Rect(int(((bodys[b]['oldX'] - centerXX) * zoom) + 420),
                                                             int(((bodys[b]['oldY'] - centerYY) * zoom) + 230), 100, 30))
