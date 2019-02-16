# Introduction

The program finds shortest path from the location chosen by the user to the nearest exit of the maze using BFS. The exits are white spaces located at the boundaries of the maze. The black blocks are obstacles to be avoided during path generation.

- If user selects obstacle, it displays information that the selected position is an obstacle and does not generate any path.
- On every user click, new path from latest location to its nearest exit is generated.

# Steps to run

- Run the python file `solve_MAZE_python.py`
- Enter the filename of the maze and press enter.
- The maze file should a text file where the first line gives dimension of the maze and is followed by the values of the maze. An example maze file named `example_maze.txt` is provided in the repository and a sample image showing the generated path is shown in `shortest_path_maze.png`.
