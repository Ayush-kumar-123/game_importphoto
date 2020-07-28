import  tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfile()
yourfilepath=file_path.name

from PIL import  Image
im= Image.open(yourfilepath)

new_size=im.resize((100,100))
new_size.save("newimage.png")

#this will allow user to import photos and even resize it


import pygame
import random
import math
import sys

pygame.init()
display = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("ayush game")

plaimg = pygame.image.load('player3.png')
fixedx = 500
fixedy = 500
player_change = 0

plaimg2 = pygame.image.load('bullet.png')
bulletx = 0
bullety = 500
bullet_changex = 0
bullet_changey = 4
bullet_state = 'ready'


def bulletfire(x, y):
    display.blit(plaimg2, (x + 16, y + 10))
    global bullet_state
    bullet_state = "fire"


def player(x, y):
    display.blit(plaimg, (x, y))

score=0

plaimg1 = pygame.image.load('newimage.png')
enemyx = random.randint(0, 936)
enemyy = random.randint(0, 200)
enemy_change = 1
enemymovex=+enemy_change
enemymovey=+enemy_change


def enemy(x, y):
    display.blit(plaimg1, (x, y))

def strike(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt(math.pow(enemyx - bulletx, 2) + (math.pow(enemyy - bullety, 2)))
    if distance < 50:
        return True
    else:
        return False


def strike2(enemyx,enemyy,fixedx,fixedy):
    distance = math.sqrt(math.pow(enemyx - fixedx, 2) + (math.pow(enemyy - fixedy, 2)))
    if distance<100:
        return True
    else:
        return False




gameon = True
while gameon:
    display.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameon = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -1

            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletx = fixedx

                    bulletfire(bulletx, bullety)
            if event.key == pygame.K_RIGHT:
                player_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0




    fixedx += player_change
    if fixedx <= 0:
        fixedx = 0
    elif fixedx >= 1000:
        fixedx = 950

    enemyx += enemymovex
    enemyy += enemymovey

    if enemyx <= 0:
        enemymovex =+enemy_change
        #enemy_change += 1
    if enemyx >= 1000:
        enemymovex =- enemy_change
        #enemy_change -= 1
    if enemyy <= 0:
        enemymovey =+ enemy_change
        #enemy_change +=1
    if enemyy >= 600:
        enemymovey =-enemy_change
        #enemy_change -= 1



    if bullety <= -50:
        bullety = 500
        bullet_state = 'ready'

    if bullet_state is 'fire':
        bulletfire(bulletx, bullety)
        bullety -= bullet_changey
    havestrike=strike(enemyx,enemyy,bulletx,bullety)
    if havestrike:
        bullety=500
        bullet_state='ready'
        score+=1
        print(score)
        enemyx = random.randint(0, 936)
        enemyy = random.randint(0, 200)
    havestrike2=strike2(enemyx,enemyy,fixedx,fixedy)
    if havestrike2:
        gameon=False
        pygame.quit()
        sys.exit()



    player(fixedx, fixedy)
    enemy(enemyx, enemyy)

    pygame.display.update()







