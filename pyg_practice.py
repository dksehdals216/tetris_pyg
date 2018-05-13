import random
import pygame
import time 

pygame.init()	#always import pygame and init to start pygame

display_width = 800
display_height = 600

# colors
black = (0, 0, 0)
white = (255, 255, 255)j
red = (255, 0 , 0)

ball_width = 111

gameDisplay = pygame.display.set_mode((display_width,display_height)) #set frame by giving tuple as param5
pygame.display.set_caption('A bit racey') # window title

clock = pygame.time.Clock() # game clock

ballImg = pygame.image.load('ball.bmp')	# load img

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def car(x, y):
	gameDisplay.blit(ballImg, (x,y)) # blit the car img

def text_objects(text, font):
	textSurface = font.render(text, True, black) # text, antialias, color, bg
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115) # font type, font size
	TextSurf, TextRect  = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2)) # x, y coords of Textbox
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()
	time.sleep(2)
	game_loop()


def crash():
	message_display('You Crashed!')


def game_loop():

	x = (display_width * 0.45)
	y = (display_height * 0.8)

	x_change = 0

	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100

	thingCount = 1

	dodged = 0
	gameExit = False 

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	# check on quit
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
					x_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

			print(event)

		x += x_change
		gameDisplay.fill(white) # fill game with white
		things(thing_startx, thing_starty, thing_width, thing_height, black)
		thing_starty += thing_speed

		thing_starty += thing_speed
		car (x, y)				# call car function
		things_dodged(dodged)
		
		if x > display_width - ball_width or x < 0:
			crash()

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, display_width)
			dodged += 1
			thing_speed += 1
			thing_width += (dodged * 1.2)

		if y < thing_starty+thing_height:
			print('y crossover')

			if x > thing_startx and x < thing_startx + thing_width or x+ball_width > thing_startx and x + ball_width < thing_startx+thing_width:		
				print('x crossover')
				crash()

		pygame.display.update() #update 1 parameter, or update whole surface without param
		#pygame.display.flip()	#
		clock.tick(60)	# param is fps


game_loop()
pygame.quit()	# ends pygame
quit()			# ends python