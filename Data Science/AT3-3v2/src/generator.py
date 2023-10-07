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

# We generate a completely connected maze that has random weight edges
# We will then use prims algorithm to generate a maze from this
def generate_max_maze(width: int, height: int) -> WeightedGraph:
    maze = WeightedGraph()

    maze.generate_graph(width * height)

    for i in range(width):
        for j in range(height):
            if i != width - 1:
                maze.connect(i + j * width, i + 1 + j * width, random.randint(1, 10))
            if j != height - 1:
                maze.connect(i + j * width, i + (j + 1) * width, random.randint(1, 10))

    print("Max maze generated")

    return maze

# returns the index of the vertex with the minimum weight edge to the current vertex
def get_minimum_weight(edges: list, visited: list):
    minimum = [float("inf"), -1]

    for edge in edges:
        if edge[0] not in visited and edge[2] < minimum[0]:
            minimum = [edge[2], edge[0], edge[1]]
        
        elif edge[1] not in visited and edge[2] < minimum[0]:
            minimum = [edge[2], edge[1], edge[0]]

    # We only need the index of the connected vertex
    return [minimum[1], minimum[2]]

# -----------------|
# Public functions |
# -----------------|

# A simple implementation of prims algorithm for generating mazes.
# Selected because of this nice visualization:
# https://en.wikipedia.org/wiki/File:MAZE_30x20_Prim.ogv

# TODO: Replace the edges list type with a set type so it runs faster
# https://wiki.python.org/moin/TimeComplexity
def prims_maze_generator(start_vertex: int, width: int, height: int):
    maze: WeightedGraph = generate_max_maze(width, height)
    
    mst = Graph()

    current_vertex = start_vertex

    edges = maze.get_connected_edges(current_vertex)

    iters = 0

    while len(mst.get_vertices()) < len(maze.get_vertices()):
        to_vertex, from_vertex = get_minimum_weight(edges, mst.get_vertices())
        
        mst.add_vertex(to_vertex)

        mst.connect(from_vertex, to_vertex)

        new_edges = maze.get_connected_edges(to_vertex)
        
        for edge in new_edges:
            if edge in edges:
                continue

            edges.append(edge)

        # Cover all cases...
        try:
            edges.remove([from_vertex, to_vertex])
            edges.remove([to_vertex, from_vertex])
        except ValueError:
            # Because we try both ways, we might try to remove an 
            # edge that doesn't exist, this should be fine...
            pass
        
        iters += 1
        print(f"Prims iterations: {iters}", end='\r')
    
    print('\n', end='')
    return mst



    

