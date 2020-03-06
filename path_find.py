import tkinter
import pygame 
from node import Node
from constants import *

# init grid columns
grid = [0 for i in range(BOARD_WIDTH)]

for i in range(BOARD_WIDTH):
	# init grid columns
	grid[i] = [0 for i in range(BOARD_HEIGHT)]

for i in range(BOARD_WIDTH):
	for j in range(BOARD_HEIGHT):
		grid[i][j] = Node(i,j)

for i in range(BOARD_WIDTH):
	for j in range(BOARD_HEIGHT):
		grid[i][j].display(WHITE, 1)

#### functions
def getStartNode():
	return startBox.get().split(',')

def getEndNode():
	return endBox.get().split(',')

def onClick():
	start = getStartNode()
	end = getEndNode()
	gui.destroy()

def pathFind():
	start.display(BLUE, 0)
	end.display(BLUE, 0)
	


#### GUI 

gui = tkinter.Tk()
gui.title('Path Finding...')
startLabel = tkinter.Label(gui, text='Hello... ')
startLabel.grid(row=0, pady=3)

endLabel = tkinter.Label(gui, text='word! ')
endLabel.grid(row=1, pady=3)

startBox = tkinter.Entry(gui)
startBox.grid(row=0, column=1, pady=3)

endBox = tkinter.Entry(gui)
endBox.grid(row=1, column=1, pady=3)

submit = tkinter.Button(gui, text='Start finding!', command=onClick)
submit.grid(row=2, column=1, pady=3)

# FIXME 
start = grid[10][25]
end = grid[40][25]
# start.display(BLUE, 0)
# end.display(BLUE, 0)

gui.update()
gui.mainloop()

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		pygame.quit()
	pygame.display.update()
	pathFind()
