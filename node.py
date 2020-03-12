import pygame 
from constants import *

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.neighbors = []
		self.weight = 1
		self.blocked = False

	def display(self, colour, n):
		pygame.draw.rect(SCREEN, colour, (self.x * WIDTH, self.y * HEIGHT, WIDTH, HEIGHT), n)
		pygame.display.update()

	def setNeighbors(self, grid):
		if self.x < WIDTH - 1 and grid[self.x + 1][self.y].blocked == False:
			self.neighbors.append(grid[self.x + 1][self.y])
		if self.x > 0 and grid[self.x -  1][self.y].blocked == False:
			self.neighbors.append(grid[self.x - 1][self.y])
		if self.y < HEIGHT - 1 and grid[self.x][self.y + 1] == False:
			self.neighbors.append(grid[self.x][self.y + 1])
		if self.y < 0 and grid[self.x][self.y - 1] == False:
			self.neighbors.append(grid[self.x][self.y - 1])
