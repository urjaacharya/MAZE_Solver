#create Maze
from Tkinter import *
master = Tk()

#Draw canvas
def draw_canvas(num_rows, num_cols):
    unitwidth = 15;
    unit_height = 15;
    canvas_width = unitwidth * num_rows + 1
    canvas_height = unit_height * num_cols + 1
    w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
    w.pack()

#read the maze file and store it in a 2D matrix
def read_file():
    
draw_canvas(20,1)
mainloop()
