from src.generator import *

# ---------------------------|
# Helper functions / classes |
# ---------------------------|

def get_adjacent_vertices(edges, current_node, maze_size):
    adjacent_vertices = []

    index = get_index_from_coordinates(current_node, maze_size)

    # Loop through all of the vertices in the row of the current node
    # and check if they are connected to the current node.
    # If so, add them to adjacent_vertices.
    for vertex in range(len(edges[index])):
        if edges[index][vertex] == 1:
            adjacent_vertices.append([vertex % maze_size[0], vertex // maze_size[1]])

    return adjacent_vertices


# If you are wondering why it takes ages to load a semi large maze, this function is why...
# We need to make a copy of the edges so we dont end up changing the original matrix.
# But that is a slow process
def traverse_graph_copy(from_node, to_node, edges, graph):

    # Convert the coordinates to an index in the adjacency matrix.
    from_index = get_index_from_coordinates(from_node, graph)
    to_index = get_index_from_coordinates(to_node, graph)

    # Basically what this does is make a copy of the matrix using the slice operator [:]. 
    # Dont ask me why it works, but its faster than a nested for loop to copy it element by element.
    edges_copy = [row[:] for row in edges]

    # Now actually traverse the graph.
    edges_copy[from_index][to_index] = 1
    edges_copy[to_index][from_index] = 1

    return edges_copy

# ----|
# DFS |
# ----|

# I had to use dfs here, it just made more sense because we make the 
# maze with it and as such it should be the best to find the solution for it.
# There isn't much commenting here as it is rather self explanatory.
def dfs(nodes, maze, edges, current_node, target, graph):

    # We want to visit the node we are currently on so we don't come here again.
    new_nodes = visit_node(current_node, nodes)

    for node in get_adjacent_vertices(maze, current_node, graph):
        if current_node == target:
            # Finally, took ages :)
            # Now hurry up and send it back down the call stack.
            return edges
        
        if was_node_visited(node, nodes):
            continue
        
        # Make a copy of the graph and then go to the next node.
        new_edges = traverse_graph_copy(current_node, node, edges, graph)

        new_edges = dfs(new_nodes, maze, new_edges, node, target, graph)

        # If the dfs chain has found the target cell, then send it back down the call stack.
        if new_edges != None:
            return new_edges
    
    return None

# ------------------------|
# Public facing functions |
# ------------------------|

def generate_solved_adjacency_matrix(maze_adjacency_matrix, maze_size):

    # This is used to store visited values
    cell_matrix = generate_maze_cell_matrix(maze_size[0], maze_size[1])

    not_yet_solved_maze = generate_maze_adjacency_matrix(maze_size[0], maze_size[1])

    solved_maze = dfs(cell_matrix, maze_adjacency_matrix, not_yet_solved_maze, [0, 0], [maze_size[0] - 1, maze_size[1] - 1], maze_size)

    if solved_maze == None:
        print("Something went wrong. generate_solved_adjacency_matrix() failed to return a solved maze.")
        exit(1)
    
    return solved_maze, cell_matrix



# ---------|
# Archived |
#----------|

# This didn't work how I needed it to, I'm leaving it here for future reference...
# As in it did work its just I didn't want to use the shortest path tree to find the 
# shortest path and instead I used a cheap simple dfs solution that just returns the 
# first path to the end node from the beginning.

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
#     # The code below is based on the pseudocode from wikipedia.
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

#     return edges
