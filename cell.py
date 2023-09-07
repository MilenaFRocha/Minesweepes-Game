from tkinter import Button, Label
import random
from settings import GRID_SIZE, CELL_COUNT


class Cell():

    all = []
    cell_count_label_object= None

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

    @staticmethod
    def create_cell_count_label(frame):
        label = Label(frame,bg = 'black', fg = 'white' , text=f"Cells left:{CELL_COUNT}" , font=("", 20))
        Cell.cell_count_label_object = label

    def left_click(self,event):
        if self.is_mine:
            self.show_mine()

        else:
            if self.surrounded_cells_mines_lenght == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
            self.show_cell()


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
        self.cell_button_object.configure(text=self.surrounded_cells_mines_lenght)

        if Cell.cell_count_label_object is not None:
            Cell.cell_count_label_object.configure(text="chaged")
        


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
    
    