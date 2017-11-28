#create Maze
from Tkinter import *

class Maze_solver:
    master = Tk()
    #variables of maze
    unitwidth = 10
    unit_height = 10
    num_rows = 0
    num_cols = 0
    grid_location_y = 0
    grid_location_x = 0
    canvas = Canvas(master,
           width=0,
           height=0)
    #Draw canvas
    def draw_canvas(self):
        canvas_height = self.unit_height * int(self.num_rows)
        canvas_width = self.unitwidth * int(self.num_cols)
        self.canvas = Canvas(self.master,
               width=canvas_width,
               height=canvas_height)
        self.canvas.pack(expand=YES, fill=BOTH)

    #read the maze file and store it in a 2D matrix
    def read_file(self):
        row_count = 0
        col_count = 0

        with open('maze.txt', 'r') as maze_file:
            lines = maze_file.readlines()
            #get number of rows and columns
            for each_line in lines: #get each line
                if (row_count == 0):
                    self.num_cols, self.num_rows = each_line.split(",")

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
        return maze

    #draw maze based on node_to_matrix
    def draw_maze(self,maze):
        for i in range(0,len(maze)):
            for j in range(0,len(maze[0])):
                if(maze[i][j] == '#'):
                    self.draw_square(j*self.unitwidth, i*self.unit_height, 'black')

    #draw square
    def draw_square(self, x_coord, y_coord, tag):
        self.canvas.create_rectangle(x_coord, y_coord, x_coord + self.unit_height-1, y_coord + self.unitwidth-1,fill=tag, outline = tag)

    #get coordinates of canvas from user click
    def callback(self,event):
        print ("clicked at", event.x, event.y)
        print ("grid location", event.x/self.unitwidth, event.y/self.unit_height)
        grid_location_x =  event.x/self.unitwidth
        grid_location_y = event.y/self.unit_height
        self.draw_square(grid_location_x*self.unitwidth, grid_location_y*self.unit_height, 'green')

    #get click from user and the location of cursor
    def user_click(self):
        #get user click
        self.canvas.bind("<Button-1>",maze_solve.callback)

#class constructor
maze_solve = Maze_solver()

#get the matrix of maze
maze = maze_solve.read_file()

#draw canvas
maze_solve.draw_canvas()

#draw maze on canvas
maze_solve.draw_maze(maze)
maze_solve.user_click()


#maze_solve.draw_square(maze_solve.grid_location_x*maze_solve.unitwidth, maze_solve.grid_location_y*maze_solve.unit_height, 'green')

mainloop()
