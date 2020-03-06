import pygame 
from constants import *

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.neighbors = []
		self.weight = 1

	def display(self, colour):
		pygame.draw.rect(SCREEN, colour, (self.x * WIDTH, self.y * HEIGHT, WIDTH, HEIGHT))
		pygame.display.update()