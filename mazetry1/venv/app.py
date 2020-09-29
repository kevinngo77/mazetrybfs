#Maze solver problem found at https://www.andrew.cmu.edu/course/15-112-n13/applications/labs/lab5/
# This function reads a maze file, filename, and creates a maze, m.
# Please declare "m" as a list before calling the function and then pass it in.
def readMaze(m, filename):
  mazeFile = open(filename, "r")
  lines = mazeFile.readlines()
  for line in lines:
    line = line.strip()
    row = [c for c in line]
    m.append(row)

m = []  # This declares the maze as an empty list
readMaze(m, "sampleMaze.txt") # This reads the maze into the list
print(m) # This prints the maze, showing it with the usual notation as a "list of lists"

mazeFile = "sampleMaze.txt"
maze = []
mazeSolution = []
index_row = 0
index_col = 0
start_x = 0
start_y = 0
end_x = 0
end_y = 0
x = 0
y = 0


#Finding the start and end points of the maze
for row in m:
  for col in row:
    if m[index_row][index_col] == 'S':
      start_x = index_row
      start_y = index_col
    if m[index_row][index_col] == 'F':
      end_x = index_row
      end_y = index_col
    index_col += 1
  index_col = 0
  index_row += 1


visited = []
frontier_queue = [[start_x, start_y]] #
index = 1 #This is the dictionary index
dictionary = {0: [1,5]} #The dictionary to reference the previous cell from the current one starting at the starting point



'''check Up then Right then Down the Left
Add current cell to visisted
If the cell next to it is not a wall and hasn't been visited then add it to queue and add the next cell to dictionary'''
for queue in frontier_queue:
    visited.append(queue)
    dictionary[index] = []
    if queue[0]-1 >= 0 and m[queue[0]-1][queue[1]] != 'W' and [queue[0]-1,queue[1]] not in visited:
        frontier_queue.append([queue[0]-1,queue[1]])
        dictionary[index].append([queue[0]-1,queue[1]])
    if queue[1]+1 <= 5 and m[queue[0]][queue[1]+1] != 'W' and [queue[0],queue[1]+1] not in visited:
        frontier_queue.append([queue[0],queue[1]+1])
        dictionary[index].append([queue[0]+1,queue[1]])
    if queue[0]+1 <= 5 and m[queue[0]+1][queue[1]] != 'W' and [queue[0]+1,queue[1]] not in visited:
        frontier_queue.append([queue[0]+1,queue[1]])
        dictionary[index].append([queue[0]+1,queue[1]])
    if queue[1]-1 >= 0 and m[queue[0]][queue[1]-1] != 'W' and [queue[0],queue[1]-1] not in visited:
        frontier_queue.append([queue[0],queue[1]-1])
        dictionary[index].append([queue[0],queue[1]-1])
    index += 1



dict_index = [end_x,end_y]
maze_Solution = [[end_x,end_y]]
#Starting at the finish works backwards to the start using the dictionary 
while dict_index != [start_x,start_y]:
    for key in dictionary:
        if dict_index in dictionary[key]:
            dict_index = frontier_queue[key-1]
            maze_Solution.append(frontier_queue[key-1])


maze_Solution.reverse()
print(maze_Solution)


