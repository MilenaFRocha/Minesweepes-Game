# Import the tkinter module thats for show in the screen the game
from tkinter import *
import settings
import utils
from cell import Cell


# Create a window called tk
root = Tk()
root.geometry(f'{settings.WIDTH}x{settings.HEIGTH}')

# Create a titte for the window
root.title("MineSweeper")

# Disable resizing the window
root.resizable(False, False)

# Change the background color
root.config(bg="black")

# Its the size and the color of the window
top_frame = Frame(root, width=utils.width_proportion(100), height=utils.height_proportion(25) , bg="black")

# this where the window is going to be
top_frame.place(    x=0, y=0)

left_frame = Frame(root, width=utils.width_proportion(25), height=utils.height_proportion(75), bg="black")
left_frame.place(x=0, y=utils.height_proportion(25))

center_frame = Frame(root, width=utils.width_proportion(75), height=utils.height_proportion(75), bg="black")
center_frame.place(x=utils.width_proportion(25), y=utils.height_proportion(25))

# make the matrix of the buttons
for x in range (settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        cell = Cell(x,y)
        # create the button object
        cell.create_button_object(center_frame)
        #put the button in  the grid
        cell.cell_button_object.grid(row=x, column=y)


Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)


Cell.randomize_mines()

# This is the main loop of the game
root.mainloop()