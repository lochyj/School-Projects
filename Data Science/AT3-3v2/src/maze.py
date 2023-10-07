import random

from lib.graph import Graph
from src.generator import prims_maze_generator
from src.solver import sp_djikstras

def generate_new_maze(maze_size: list[int, int]):

    maze: Graph = prims_maze_generator(0, maze_size[0], maze_size[1])

    print("Maze generated")

    shortest_path: list[int] = sp_djikstras(maze, 0, maze_size[0] * maze_size[1] - 1)

    print("Shortest path found")

    return [maze, shortest_path]

