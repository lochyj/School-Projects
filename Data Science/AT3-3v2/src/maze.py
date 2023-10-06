import random

from lib.graph import Graph

# Maze is an extension of Graph and simply modifies the get_adjacent_vertices to give a random list of adjacent vertices
class Maze(Graph):
    def get_adjacent_vertices(self, vertex, width, height):
        x = vertex % width
        y = vertex // width

        adjacent = []

        if x != 0:
            adjacent.append(vertex - 1)

        if x != width:
            adjacent.append(vertex + 1)

        if y != 0:
            adjacent.append(vertex - width)
        
        if y != height:
            adjacent.append(vertex + width)

        # Well, Well, Well, something went wildly wrong
        if len(adjacent) == 0:
            print("Something went wrong in Maze.get_adjacent_vertices")
            exit(1)

        return random.choice(adjacent)