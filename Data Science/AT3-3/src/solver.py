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


# Thanks wikipedia :) (https://en.wikipedia.org/wiki/Amortized_analysis)

class Queue:
    # Define the constructor method that initializes two empty lists
    def __init__(self):
        self.input = [] # This list will store the elements that are enqueued
        self.output = [] # This list will store the elements that are dequeued

    # Define a method named enqueue that takes an element as a parameter
    def enqueue(self, element):
        self.input.append(element) # Append the element to the input list

    # Define a method named dequeue that returns the first element that was enqueued
    def dequeue(self):
        if not self.output: # If the output list is empty
            while self.input: # While the input list is not empty
                self.output.append(self.input.pop()) # Pop the last element from the input list and append it to the output list

        return self.output.pop() # Pop and return the last element from the output list

    # I added this...
    def is_empty(self):
        if len(self.input) == 0 and len(self.output) == 0:
            return True

        return False

# ----|
# BFS |
#-----|

def bfs(nodes, edges, maze, current_node, goal_node, graph):
    # TODO
    # https://en.wikipedia.org/wiki/Breadth-first_search

    Q = Queue()

    nodes = visit_node(current_node, nodes)

    Q.enqueue([0, 0])

    while not Q.is_empty():
        v = Q.dequeue()

        if v == goal_node:
            break

        for w in get_adjacent_vertices(maze, v, graph):
            if was_node_visited(w, nodes):
                continue

            nodes = visit_node(w, nodes)
            edges = traverse_graph(v, w, edges, graph)
            Q.enqueue(w)

    # make a new edge matrix and only load the path into it
    solved_matrix = generate_maze_adjacency_matrix(graph[0], graph[1])

    for i, cell in enumerate(edges):
        for j, connected_cell in enumerate(cell):
            if connected_cell == 1:
                solved_matrix[i][j] = 1

    return solved_matrix, edges


# ------------------------|
# Public facing functions |
# ------------------------|

def generate_solved_adjacency_matrix(maze_adjacency_matrix, maze_size):
    cell_matrix = generate_maze_cell_matrix(maze_size[0], maze_size[1])

    solved_maze = generate_maze_adjacency_matrix(maze_size[0], maze_size[1])

    return bfs(cell_matrix, solved_maze, maze_adjacency_matrix, [0, 0], [maze_size[0] - 1, maze_size[1] - 1], maze_size)