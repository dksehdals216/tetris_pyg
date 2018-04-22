import pygame

pygame.init()	#always import pygame and init to start pygame

display_width = 800
display_height = 600

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 , 0)

gameDisplay = pygame.display.set_mode((display_width,display_height)) #set frame by giving tuple as param5
pygame.display.set_caption('A bit racey') # window title

clock = pygame.time.Clock() # game clock

ballImg = pygame.image.load('ball.bmp')	# load img

def car(x, y):
	gameDisplay.blit(ballImg, (x,y)) # blit the car img


x = (display_width * 0.45)
y = (display_height * 0.8)


crashed = False 

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	# check on quit
			crashed = True

		print(event)

	gameDisplay.fill(white) # fill game with white
	car (x, y)				# call car function
	pygame.display.update() #update 1 parameter, or update whole surface without param
	#pygame.display.flip()	#
	clock.tick(60)	# param is fps

pygame.quit()	# ends pygame
quit()			# ends python