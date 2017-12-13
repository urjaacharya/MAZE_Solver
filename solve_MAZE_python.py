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
    src_node_num = -1
    maze = [[]]
    #Draw canvas
    def draw_canvas(self):
        canvas_height = self.unit_height * int(self.num_rows)
        canvas_width = self.unitwidth * int(self.num_cols)
        self.canvas = Canvas(self.master,
               width=canvas_width,
               height=canvas_height)
        self.canvas.pack(expand=YES, fill=BOTH)

    #read the maze file and store it in a 2D matrix
    def read_file(self, file_name):
        row_count = 0
        col_count = 0

        with open(file_name, 'r') as maze_file:
            lines = maze_file.readlines()
            #get number of rows and columns
            for each_line in lines: #get each line
                if (row_count == 0):
                    self.num_cols, self.num_rows = each_line.split(",")

                    #initialize maze
                    self.maze = []
                else:
                    self.maze.append([]);
                    #get each character
                    for each_char in each_line:
                        if (each_char != '\n'):
                            self.maze[row_count-1].append(each_char)
                    col_count = col_count + 1;
                row_count = row_count + 1;
        return self.maze

    #draw maze based on node_to_matrix
    def draw_maze(self,maze):
        for i in range(0,int(self.num_rows)):
            for j in range(0, int(self.num_cols)):
                if(self.maze[i][j] == '#'):
                    self.draw_square(j*self.unitwidth, i*self.unit_height, 'black')
                else:
                    self.draw_square(j*self.unitwidth, i*self.unit_height, 'white')

    #draw square
    def draw_square(self, x_coord, y_coord, tag):
        self.canvas.create_rectangle(x_coord, y_coord, x_coord + self.unit_height-1, y_coord + self.unitwidth-1,fill=tag, outline = tag)

    #get coordinates of canvas from user click
    def callback(self,event):
        self.grid_location_x =  event.x/self.unitwidth
        self.grid_location_y = event.y/self.unit_height
        #only find shortest path if the clicked cell is white
        if(maze[self.grid_location_y][self.grid_location_x] == '#'):
            self.draw_maze(self.maze)
            print ('It is an obstacle, click on the hallway (i.e white area)')

        else:
            #convert the grid to node Number
            self.src_node_num = int(self.grid_location_y)*int(self.num_cols) + int(self.grid_location_x)
            print ("node", self.src_node_num)
            #find shortest path and draw it
            self.draw_maze(self.maze)
            curr, parent = self.shortest_path()
            self.draw_short_path(curr, parent)

        #self.draw_square(self.grid_location_x*self.unitwidth, self.grid_location_y*self.unit_height, 'green')

    #get click from user and the location of cursory
    def user_click(self):
        #get user click
        self.canvas.bind("<Button-1>", self.callback)
        return self.grid_location_x, self.grid_location_y

    def node_num_to_indexes(self,node_num):
        index_y = node_num/int(self.num_cols)
        index_x = node_num - index_y*int(self.num_rows)
        return index_x, index_y

    #check if a node is an exit
    def is_exit(self,index_x, index_y):
        if (index_x == 0 or index_x == int(self.num_cols)-1 or index_y == 0 or index_y == int(self.num_rows)-1):
            return 1
        return 0

    #check node validity
    def check_validity(self, curr_node, row_index, adj_node):
        diff = curr_node - adj_node
        upper_index = row_index+1
        if (abs(diff) == 1 and (adj_node >= row_index * int(self.num_cols)) and (adj_node < (upper_index*int(self.num_cols)))):
            return 1
        elif ((abs(diff) != 1) and (adj_node < int(self.num_cols) * int(self.num_rows)) and (adj_node >= 0)):
            return 1
        return 0

    #draw the path to exit
    def draw_short_path(self,current_node, parent_node):
        print (current_node)
        while(current_node != -1):
            print (current_node)
            x_coord, y_coord = self.node_num_to_indexes(current_node)
            self.draw_square(x_coord*self.unitwidth, y_coord*self.unit_height, 'green')
            current_node = parent_node[current_node]

    #find shortest path to exist
    def shortest_path(self):
        #to find adjacent nodes
        adj_values = [1,-1,self.num_cols, -int(self.num_cols)]
        #queue for BFS
        queue = []
        #set parent node also put visited to 0 (to signify not visited)
        visited = []
        parent_node = []
        for i in range(int(self.num_cols)*int(self.num_rows)):
            visited.append(0)
            parent_node.append(-1)
        #add source node to queue
        queue.append(self.src_node_num)
        #set it to visited
        visited[self.src_node_num] = 1

        #until quue gets empty
        while(len(queue) > 0):
            curr_node = queue[0] #get the first element in the queue
            #print ("curr", curr_node)
            #remove element from queue
            queue.remove(curr_node)
            index_curr_x, index_curr_y = self.node_num_to_indexes(curr_node)
            print("x,y", index_curr_x, index_curr_y)
            #if exit is reached, stop
            if (self.is_exit(index_curr_x, index_curr_y)):
                return curr_node, parent_node

            #get adjacent nodes
            for i in range(len(adj_values)):
                adj_node = curr_node + int(adj_values[i])
                print (adj_node, "adj")
                #check validity of nodes
                if(self.check_validity(curr_node,index_curr_y,adj_node)):
                    #print(adj_node,",")
                    index_adj_x, index_adj_y = self.node_num_to_indexes(adj_node)
                    #if not is not visited before and is not an obstacle
                    if(visited[adj_node] == 0 and self.maze[index_adj_y][index_adj_x] != '#'):
                        visited[adj_node] = 1
                        parent_node[adj_node] = curr_node
                        #add the node to queue
                        queue.append(adj_node)
        return -1, [-1] # if no path exits

#class constructor
maze_solve = Maze_solver()

name_file = raw_input("Enter the filename: ")
#get the matrix of maze
maze = maze_solve.read_file(name_file)

#draw canvas
maze_solve.draw_canvas()

#draw maze on canvas
maze_solve.draw_maze(maze)
maze_solve.user_click()

#maze_solve.draw_square(maze_solve.grid_location_x*maze_solve.unitwidth, maze_solve.grid_location_y*maze_solve.unit_height, 'green')

mainloop()
