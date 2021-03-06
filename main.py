
'''

RULES:
    1. All tetrominoes spawn horizontall and wholly above the playfield
    2. I, O tetrominoes spawn centrally, while 3-cell wide tetrominoes spawn rounded to the left
    3. J, L, T spawn flat-side first
  
'''
import pygame
import time
from time import sleep
import random
import math

from block_sh import sh_pick

pygame.init()

#pixels
BLOCK_DIM = 24
BOARD_W = 10
BOARD_H = 22

display_width = BLOCK_DIM * BOARD_W
display_height = BLOCK_DIM * BOARD_H

BLOCK_N = 7

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 , 0)


gameDisplay = pygame.display.set_mode((display_width,display_height)) #set frame by giving tuple as param5
pygame.display.set_caption('Tetris') # window title

clock = pygame.time.Clock() # game clock
game_cond = False
                                                        #Color  #.  Reference
                                                        #white 	0
blue_bl = pygame.image.load('img/blue_block.png')       #blue 	1 	O
cyan_bl = pygame.image.load('img/cyan_block.png')       #cyan 	2 	I
green_bl = pygame.image.load('img/green_block.png')     #green 	3 	L
purple_bl = pygame.image.load('img/purple_block.png')   #purple 4	Z
red_bl = pygame.image.load('img/red_block.png')         #red 	5 	J
turq_bl = pygame.image.load('img/turq_block.png')       #turq 	6 	S
yellow_bl = pygame.image.load('img/yellow_block.png')   #yellow 7 	T

#init 22x10, height x width matrix to 0
matrix_tetris = [[0] * BOARD_W for i in range(BOARD_H)]

def draw_obj(img_n, x, y):
    gameDisplay.blit(img_n, (x, y))


def draw_Board(matrix):
    for x in range(BOARD_H):
        for y in range(BOARD_W):
            if matrix[x][y] != 0:
                draw_obj(blue_bl, x*BLOCK_DIM, y*BLOCK_DIM)

#draws matrix into matrix_tetris onto x, y coordinates
def draw_sh_matrix(matrix, x, y):
    for i in range(len(matrix)):
        #fix this 
        for j in range(int(math.sqrt(len(matrix)))):
            print(i, j)
            if matrix[i][j] == 1:
                matrix_tetris[x + i][y + j] = 1

def free_matrix(matrix, x, y):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                matrix_tetris[x + i][y + j] = 0

#0 left, 1 down, 2 right
#todo: implement different tetrominoes as input
def update_on_keypress(dir, x, y):
    #free_matrix(sh_pick(1, 0), x, y)
    if dir == 0:
        draw_sh_matrix(sh_pick(1, 0),x - 1, y)
    if dir == 1:
        draw_sh_matrix(sh_pick(1, 0),x, y + 1)
    if dir == 2:
        draw_sh_matrix(sh_pick(1, 0),x + 1, y)

x = 0
y = 0
free_block = True   #block that is still moving

while not game_cond:
    gameDisplay.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cond = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_cond = True
#fix speed, different keypress and implement rotation
            if free_block == True:
                if event.key == pygame.K_DOWN:
                    update_on_keypress(1, x, y)
                    draw_Board(matrix_tetris)
                    y += 1
                if event.key == pygame.K_RIGHT:
                    draw_Board(matrix_tetris)

                if event.key == pygame.K_LEFT:
                    draw_Board(matrix_tetris)

    pygame.display.update()
    clock.tick(1)

pygame.quit()   # ends pygame
quit()          # ends python
