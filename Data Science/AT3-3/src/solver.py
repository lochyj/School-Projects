from src.generator import *


# ---------------------------|
# Helper functions / classes |
# ---------------------------|

def get_index_from_coordinates(coordinates, maze_size):
    return (coordinates[1] * maze_size[0] + coordinates[0])

def get_adjacent_vertices(edges, current_node, maze_size):
    adjacent_vertices = []

    index = get_index_from_coordinates(current_node, maze_size)

    for vertex in range(len(edges[index])):
        if edges[index][vertex] == 1:
            adjacent_vertices.append([vertex % maze_size[0], vertex // maze_size[1]])

    return adjacent_vertices


# If you are wondering why it takes ages to load a semi large maze, this function is why...
# We need to make a copy of the edges so we dont end up changing the original matrix.
# But that is a slow process
def traverse_graph_copy(from_node, to_node, edges, graph):
    width = graph[0]
    height = graph[1]

    from_index = from_node[1] * width + from_node[0]
    to_index = to_node[1] * width + to_node[0]

    # Basically what this does is make a copy of the matrix using the slice operator [:]. 
    # Dont ask me why it works, but its faster than a nested for loop to copy it element by element.
    # O(n^2) is the best we can do with python's system. (n is the width * height of the maze)
    edges_copy = [row[:] for row in edges]

    edges_copy[from_index][to_index] = 1
    edges_copy[to_index][from_index] = 1

    return edges_copy


# This didnt work how I needed it to, im leaving it here for future reference...

# Thanks wikipedia :) (https://en.wikipedia.org/wiki/Amortized_analysis)

# class Queue:
#     # Define the constructor method that initializes two empty lists
#     def __init__(self):
#         self.input = [] # This list will store the elements that are enqueued
#         self.output = [] # This list will store the elements that are dequeued

#     # Define a method named enqueue that takes an element as a parameter
#     def enqueue(self, element):
#         self.input.append(element) # Append the element to the input list

#     # Define a method named dequeue that returns the first element that was enqueued
#     def dequeue(self):
#         if not self.output: # If the output list is empty
#             while self.input: # While the input list is not empty
#                 self.output.append(self.input.pop()) # Pop the last element from the input list and append it to the output list

#         return self.output.pop() # Pop and return the last element from the output list

#     # I added this...
#     def is_empty(self):
#         if len(self.input) == 0 and len(self.output) == 0:
#             return True

#         return False


# ----|
# BFS |
#-----|

# def bfs(nodes, edges, maze, current_node, goal_node, graph):
#     # TODO
#     # https://en.wikipedia.org/wiki/Breadth-first_search

#     Q = Queue()

#     nodes = visit_node(current_node, nodes)

#     Q.enqueue([0, 0])

#     while not Q.is_empty():
#         v = Q.dequeue()

#         if v == goal_node:
#             break

#         for w in get_adjacent_vertices(maze, v, graph):
#             if was_node_visited(w, nodes):
#                 continue

#             nodes = visit_node(w, nodes)
#             edges = traverse_graph(v, w, edges, graph)
#             Q.enqueue(w)

#     # make a new edge matrix and only load the path into it
#     solved_matrix = generate_maze_adjacency_matrix(graph[0], graph[1])

#     for i, cell in enumerate(edges):
#         for j, connected_cell in enumerate(cell):
#             if connected_cell == 1:
#                 solved_matrix[i][j] = 1

#     return solved_matrix, edges

# ---



# ----|
# DFS |
# ----|

# I had to use dfs here, it just made more sense because we make the maze with it and as such it should be the best to find the solution for it.
def dfs(nodes, maze, edges, current_node, target, graph):
    new_nodes = visit_node(current_node, nodes)

    for node in get_adjacent_vertices(maze, current_node, graph):
        if current_node == target:
            return edges

        if was_node_visited(node, nodes):
            continue

        new_edges = traverse_graph_copy(current_node, node, edges, graph)
        new_edges = dfs(new_nodes, maze, new_edges, node, target, graph)

        if new_edges != None:
            return new_edges
    
    return None

# ------------------------|
# Public facing functions |
# ------------------------|

def generate_solved_adjacency_matrix(maze_adjacency_matrix, maze_size):
    cell_matrix = generate_maze_cell_matrix(maze_size[0], maze_size[1])

    solved_maze = generate_maze_adjacency_matrix(maze_size[0], maze_size[1])

    solved_maze = dfs(cell_matrix, maze_adjacency_matrix, solved_maze, [0, 0], [maze_size[0] - 1, maze_size[1] - 1], maze_size)

    if solved_maze == None:
        exit(1)
    
    return solved_maze, cell_matrix