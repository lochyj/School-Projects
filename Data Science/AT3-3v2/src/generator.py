# ---------|
# Includes |
# ---------|

# ---------
# 3rd Party
# ---------

import random

# ---------
# Home made
# ---------

from lib.graph import Graph
from lib.weighted_graph import WeightedGraph

# -----------------|
# Helper functions |
# -----------------|

# Converts an index of a vertex in a graph to its coordinates
def index_to_coords(index: int, width: int, height: int):
    return (index % width, index // width)

# Converts the coordinates of a vertex to its index in a graph
def coords_to_index(coords: tuple[int, int], width: int, height: int):
    return coords[0] + coords[1] * width

def generate_max_maze(width: int, height: int) -> WeightedGraph:
    maze = WeightedGraph()

    maze.generate_graph(width * height)

    for i in range(width):
        for j in range(height):
            if i != width - 1:
                maze.connect(i + j * width, i + 1 + j * width, random.randint(1, 10))
            if j != height - 1:
                maze.connect(i + j * width, i + (j + 1) * width, random.randint(1, 10))
    
    return maze

def get_minimum_weight(edges: list):
        minimum = [float("inf"), -1]

        for edge in edges:
            if edge[2] < minimum:
                minimum = [edge[2], [edge[0], edge[1]]]

        return minimum
    

# -----------------|
# Public functions |
# -----------------|

# A simple implementation of prims algorithm for generating mazes.
# Selected because of this nice visualization:
# https://en.wikipedia.org/wiki/File:MAZE_30x20_Prim.ogv
def prims_maze_generator(start_vertex: int, width: int, height: int):
    maze: WeightedGraph = generate_max_maze(width, height)
    
    mst = Graph()

    edges = maze.get_adjacent_vertices(start_vertex)

    while len(mst) < len(maze.get_vertices()):
        weight, edge = maze.get_minimum_weight(edges)
        ...

    

