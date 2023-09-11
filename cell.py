from tkinter import Button, Label
import random
from settings import GRID_SIZE, CELL_COUNT, MINE_CHOSED
import ctypes
import sys


class Cell():

    all = []
    cell_count_label_object= None
    cell_count =CELL_COUNT

    def __init__(self,x,y,is_mine = False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_mine_candidate = False
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

    @staticmethod
    def create_cell_count_label(frame):
        label = Label(frame,bg = 'black', fg = 'white' , text=f"Cells left:{Cell.cell_count}" , font=("", 20))
        Cell.cell_count_label_object = label

    def left_click(self,event):
        if self.is_mine:
            self.show_mine()

        else:
            if self.surrounded_cells_mines_lenght == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
            self.show_cell()

            if Cell.cell_count == MINE_CHOSED:
                ctypes.windll.user32.MessageBoxW(0,"You won","Game Over",0)
                sys.exit()

        self.cell_button_object.unbind('<Button-1>')
        self.cell_button_object.unbind('<Button-3>')


    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1),

        ]
        cells = [cell for cell in cells if cell is not None]   
        return cells
    

    @property
    def surrounded_cells_mines_lenght(self):
        counter =0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter +=1

        return counter

    
    def show_cell(self):  
        if not self.is_open:


            Cell.cell_count -=1
            self.cell_button_object.configure(text=self.surrounded_cells_mines_lenght)

            if Cell.cell_count_label_object is not None:
                Cell.cell_count_label_object.configure( text=f"Cells left:{Cell.cell_count}")

            self.cell_button_object.configure(bg="SystemButtonFace")
        self.is_open = True


        


    def show_mine(self):
        self.cell_button_object.config(text="*",bg="red")
        ctypes.windll.user32.MessageBoxW(0,"You clicked on a mine","Game Over",0)
        sys.exit()
    

    def right_click(self,event):
        if not self.is_mine_candidate:
           self.cell_button_object.configure(
               bg= 'orange'
           )
           self.is_mine_candidate = True

        else:
            self.cell_button_object.configure(
                bg='SystemButtonFace'
           )
            self.is_mine_candidate = False


    @staticmethod
    def randomize_mines():
        list_of_cells = Cell.all
        mines = random.sample(list_of_cells, GRID_SIZE)
        for mine in mines:
            mine.is_mine = True
            

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
    
    