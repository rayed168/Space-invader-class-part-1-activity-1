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

player_img=pg.image.load("player.png")
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
score_font=pg.font.Font("freesansbold.ttf",60)
text_x=10
text_y=10
game_over_font=pg.font.Font("freesansbold.ttf",90)

def show_score(x,y):
    score_image=score_font.render("Score: " + str(score),True,(255,255,255))
    screen.blit(score_image,(x,y))
def game_over():
    game_over_image=game_over_font.render("GAME OVER!",True,(255,0,0))
    screen.blit(game_over_image,(200,250))
def player(x,y):
    screen.blit(player_img,(x,y))
def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))
def is_collision(enemy_x,enemy_y,bullet_x,bullet_y):
     distance = mt.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)
     return distance < COLLISION_DISTANCE
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN:
            if event.type==pg.K_LEFT:
                player_x_change=-5
            if event.type==pg.K_RIGHT:
                player_x_change=+5
            if event.type==pg.K_SPACE and bullet_state=="ready":
                bullet_x=player_x
                fire_bullet(bullet_x,bullet_y)
        if event.type==pg.KEYUP and event.key in [pg.K_RIGHT,pg.K_LEFT]:
            player_x_change=0
    player_x=player_x+player_x_change
    player_x=max(0,min(player_x,SCREEN_WIDTH-64))
    for i in range(number_of_enemies):
        if enemy_y[i] > 340: 
            for j in range(number_of_enemies):
                enemy_y[j] = 2000
            game_over_font()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_y[i] >= SCREEN_WIDTH - 64:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]   
        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = PLAYER_START_Y
            bullet_state = "ready"
            score += 1
            enemy_x[i] = rn.randint(0, SCREEN_WIDTH - 64)
            enemy_y[i] = rn.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemy(enemy_x[i], enemy_y[i], i) 
    if bullet_y <= 0:
        bullet_y = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    player(player_x, player_y)
    show_score(text_x,text_y)
    pg.display.update()
    