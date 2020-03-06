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

start = grid[1][2]

for i in range(BOARD_WIDTH):
	for j in range(BOARD_HEIGHT):
		grid[i][j].display(PINK)

print('done 1')

#### GUI 

gui = tkinter.Tk()
startLabel = tkinter.Label(gui, text='Hello... ')
startLabel.grid(row=0, pady=3)

endLabel = tkinter.Label(gui, text='word! ')
endLabel.grid(row=1, pady=3)

startBox = tkinter.Entry(gui)
startBox.grid(row=0, column=1, pady=3)

endBox = tkinter.Entry(gui)
endBox.grid(row=1, column=1, pady=3)

# command takes in a function
# submit = tkinter.Button(gui, text='Start finding!', command=)
# submit.grid(row=2, column=1, pady=3)

gui.update()
gui.mainloop()
print('done 2')
SCREEN.fill(pygame.Color(255,255,255))
pygame.display.init()