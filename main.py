
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

import block_sh

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
blue_bl = pygame.image.load('img/blue_block.png') 		#blue 	1 	O
cyan_bl = pygame.image.load('img/cyan_block.png')		#cyan 	2 	I
green_bl = pygame.image.load('img/green_block.png') 	#green 	3 	L
purple_bl = pygame.image.load('img/purple_block.png')	#purple 4	Z
red_bl = pygame.image.load('img/red_block.png')			#red 	5 	J
turq_bl = pygame.image.load('img/turq_block.png')		#turq 	6 	S
yellow_bl = pygame.image.load('img/yellow_block.png')	#yellow 7 	T

#init 22x10, height x width matrix to 0
matrix_tetris = [[0] * BOARD_W for i in range(BOARD_H)]

'''
def clear(matrix):
    for x in range(BOARD_H):
        for y in range(BOARD_W):
            matrix[x][y] = 0
'''
def draw_obj(img_n, x, y):
	gameDisplay.blit(img_n, (x, y))

#def draw_shape(img_arr, x, y):

def draw_Board(matrix):
	for x in range(BOARD_H):
		for y in range(BOARD_W):
			if matrix[x][y] != 0:
				draw_obj(blue_bl, x*BLOCK_DIM, y*BLOCK_DIM)
    
x =  (0)
y = (0)

while not game_cond:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_cond = True

	matrix_tetris[0][0] = 1 
	matrix_tetris[1][1] = 1
	gameDisplay.fill(black)
	draw_Board(matrix_tetris)

	pygame.display.update()
	clock.tick(1)

pygame.quit()	# ends pygame
quit()			# ends python
