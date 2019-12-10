Depth First Search (DFS)

- An algorithm used to search a graph
- explores all possible paths to find one with smallest weight, traversing down a branch before traversing the same level
- will start at the root node similar to BFS
- uses a stack() first in last out

Uses

- Works well finding connected or strongly connected components within bigger graphs
- A situation where it's known that there's only one solution
- Works better with situations with one solution because follows a complete path, then the next complete path

The algorithm

1. Begin at starting vertex(s)
2. explore vertex
    1. if unexplored, adjacent vertex:
        - explore adjacent vertex
    2. mark explored once all adjacent vertices have been explored (remove from stack)

Summary

- We can use DFS to traverse a graph, searching each branch to it's deepest level before exploring another branch
- This is a algorithm when you know the solution is very far from the root


Breadth First Search (BFS)

- algorithm used to search a graph
- Explores all possible paths to find one with the smallest weight, traversing across before traversing down
- Never revisits nodes
- uses a queue() first in first out

Uses
- Very useful for route-finding or path finding (explores routes or roads closest to each-other)
- Useful for social networking site (showing how far apart connections are via mutual friends ect)

The algorithm

1. Begin at starting vertex(s)
2. explore vertex
    1. while +1 unscheduled vertices adjacent to current vertex 
        - schedule adjacent vertex to be explored (queue)
3. mark the vertex as explored remove from queue

Summary

- we can use BFS to traverse a graph, starting at levels closest to the root and finishing at those furthest away
- good if you are solving a derivative of the shortest path problem or any other scenario where you know the solution is not far from the root 