'''
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
'''



islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4

def get_neighbors(vertex,graph_matrix):
    x= vertex[0]
    y = vertex[1]
    neighbors = []
    # check north
    if y > 0 and graph_matrix[y-1][x] == 1:
        neighbors.append((x,y-1))
    # check south
    if y < len(graph_matrix) - 1 and graph_matrix[y+1][x] == 1
    # check east
    # check west

def bft(x,y,matrix,visited):
    q=Queue()
    q.enqueue((x,y))
    while q.size() > 0:
        v = q.dequeue()
        x = v[0]
        y = v[1]
        if not visited[y][x]:
            visited[x][y] = True
            for neighbor in get_neighbors((x,y),matrix):
                q.enqueue(next_vert)


# translate the problem into graphs terminology
# Build your graph
# Traverse your graph
def island_counter(islands)
# loop through the islands
# do bfs on them and count how many times the bft occurs
# created a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False]* len(matrix[0]))
# create a counter, initialize to 0
    island_counter = 0
# walk though each cell in the matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
    # if it has not been visited:
            if not visited [y][x]:
        # if you reach a 1:
                if matrix[y][x] == 1:
            # do a BFT and mark each 1 as visited
                    visited = bft(x,y,matrix,visited)
            # Increment counter by 1 
