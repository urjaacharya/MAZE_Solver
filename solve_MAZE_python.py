#create Maze
from Tkinter import *
master = Tk()

#Draw canvas
def draw_canvas(num_rows, num_cols):
    unitwidth = 15;
    unit_height = 15;
    canvas_height = unit_height * num_rows + 1
    canvas_width = unitwidth * num_cols + 1
    w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
    w.pack()

#read the maze file and store it in a 2D matrix
def read_file():
    row_count = 0
    col_count = 0

    with open('maze.txt', 'r') as maze_file:
        lines = maze_file.readlines()
        #get number of rows and columns
        for each_line in lines: #get each line
            if (row_count == 0):
                num_cols, num_rows = each_line.split(",")
                print (num_cols)
                #initialize maze
                maze = []
            else:
                maze.append([]);
                #get each character
                for each_char in each_line:
                    if (each_char != '\n'):
                        maze[row_count-1].append(each_char)
                col_count = col_count + 1;
            row_count = row_count + 1;
        #print the maze matrix (or, 2d list)
        print (maze)

draw_canvas(20,1)
read_file()
mainloop()
