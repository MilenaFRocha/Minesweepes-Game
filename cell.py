from tkinter import Button
import random
from settings import GRID_SIZE


class Cell():

    all = []

    def __init__(self,x,y,is_mine = False):
        self.is_mine = is_mine
        self.cell_button_object = None
        self.x = x
        self.y = y

    # Append the cell to the list
        Cell.all.append(self)


    def create_button_object(self,frame):
        button = Button (frame, width=12,height=4)

        button.bind("<Button-1>", self.left_click)
        button.bind("<Button-3>", self.right_click)

        self.cell_button_object=button

    def left_click(self,event):
        if self.is_mine:
            self.show_mine()

        else:
            self.show_cell()

    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
        

    def show_cell(self):
        print(self.get_cell_by_axis(self.x,self.y))


    def show_mine(self):
        self.cell_button_object.config(text="*",bg="red")
    

    def right_click(self,event):
        print(event)
        print("Right click")

    @staticmethod
    def randomize_mines():
        list_of_cells = Cell.all
        mines = random.sample(list_of_cells, GRID_SIZE)
        for mine in mines:
            mine.is_mine = True
            

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
    
    