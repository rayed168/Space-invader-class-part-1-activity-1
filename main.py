import pygame as pg
import random as rn
import math as mt 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pg.init()
screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background=pg.image.load("background.png")
pg.display.set_caption("Space Invaders")
pg.display.set_icon("player.png")

player=pg.image.load("player.png")
player_x=PLAYER_START_X
player_y=PLAYER_START_Y
player_x_change=0

enemy_img=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
number_of_enemies=6

for _i in range(number_of_enemies):
    enemy_img.append(pg.image.load("enemy.png"))
    enemy_x.append(rn.randint(0,SCREEN_WIDTH-64))
    enemy_y.append(rn.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemy_x_change.append(ENEMY_SPEED_X)
    enemy_y_change.append(ENEMY_SPEED_Y)

bullet=pg.image.load("bullet.png")
bullet_x=0
bullet_y=PLAYER_START_Y
bullet_x_change=0
bullet_y_change=BULLET_SPEED_Y
bullet_state="ready"

score=0
font=pg.font.Font("freesansbold.ttf",60)
text_x=10
text_y=10
game_over_font=pg.font.Font("freesansbold.ttf",90)
