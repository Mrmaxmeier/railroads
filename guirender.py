#Pygame Needed...
import pygame

class GUI:
	pygame.init()
	screen = pygame.display.set_mode((1920, 1080))
	screensize = [1920, 1080]
	pygame.display.set_caption('Railroads!')
	running = True

class Renderer(GUI):