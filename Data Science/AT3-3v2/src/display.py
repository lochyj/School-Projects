# ---------|
# Includes |
# ---------|

# ---------
# 3rd Party
# ---------

import pygame
import pygame_gui

# ---------
# Home made
# ---------

from lib.graph import Graph

from src.constants import *

# -----------------|
# Helper functions |
# -----------------|

def draw_cell(coords: list[int, int], cell_size: list[int, int], window: pygame.Surface, colour: tuple[int, int, int]):
    cell_width = cell_size[WIDTH]
    cell_height = cell_size[HEIGHT]

    # Convert the x and y index value to the x and y pixel value
    x = coords[WIDTH] * cell_width * 2
    y = coords[HEIGHT] * cell_height * 2

    pygame.draw.rect(window, colour, (x, y, cell_width, cell_height), 0)

# This is the worst function ever written
# There are many things about this function that are terrible
# One is that I have no idea why it doesn't output the expected 
# values 100% of the time and the other is that there are a 
# number of useless calls to this function that i have to filter out.
# I might fix this another time... probably not.
def draw_edge(from_vertex: list[int, int], to_vertex: list[int, int], cell_size: list[int, int], window: pygame.Surface, colour: tuple[int, int, int]):
    if from_vertex == to_vertex:
        return
    
    cell_width = cell_size[WIDTH]
    cell_height = cell_size[HEIGHT]

    dx = 0
    dy = 0

    # Get the delta of the edge
    # For example, if from_vertex is 
    # below to_vertex, we need to 
    # render it above from_vertex.
    # so that the edge connects the two properly.
    # That is poorly explained hopefully 
    # you can understand it
    if from_vertex[X] < to_vertex[X]:
        dx = cell_width
    elif from_vertex[Y] > to_vertex[Y]:
        dx = -cell_width

    if from_vertex[Y] < to_vertex[Y]:
        dy = cell_height
    elif from_vertex[Y] > to_vertex[Y]:
        dy = -cell_height

    # This sometimes happens?
    if dx == 0 and dy == 0 or abs(dx + dy) == cell_width + cell_height:
        return
    
    # Get pixel position of the topleft of the cell
    x = (from_vertex[X] * cell_width * 2) + dx
    y = (from_vertex[Y] * cell_height * 2) + dy

    pygame.draw.rect(window, colour, (x, y, cell_width, cell_height))


# Converts an index of a vertex in a graph to its coordinates
def index_to_coords(index: int, width: int):
    return [index % width, index // width]

# Converts the coordinates of a vertex to its index in a graph
def coords_to_index(coords: list[int, int], width: int):
    return int(coords[0] + coords[1] * width)

# -----------------|
# Public functions |
# -----------------|

def init_window(width: int, height: int, theme_dir: str):
    pygame.display.set_caption("aMazing software")

    # Create the pygame window
    window = pygame.display.set_mode((width, height))

    window.fill(BLACK)  # The background colour is BLACK

    gui_manager = pygame_gui.UIManager((width, height), theme_dir)  # Set 

    return [window, gui_manager]

def draw_maze(maze: Graph, shortest_path: list[int], maze_size: list[int, int], window: pygame.Surface):
    # The size of the cells in the maze, in pixels.
    # It is simply the size of the maze / the number of 
    # cells / 2 because we need space for edges also
    cell_size = [MAZE_WINDOW[WIDTH] / maze_size[WIDTH] / 2, MAZE_WINDOW[HEIGHT] / maze_size[HEIGHT] / 2]

    # Draw the vertices of the maze
    for i in range(maze_size[HEIGHT]):
        for j in range(maze_size[WIDTH]):
            draw_cell([j, i], cell_size, window, WHITE)
    
    # Draw the edges of the maze
    for i in range(maze_size[HEIGHT]):
        for j in range(maze_size[WIDTH]):
            for vertex in maze.get_adjacent_vertices(coords_to_index([j, i], maze_size[WIDTH])):
                draw_edge([j, i], index_to_coords(vertex, maze_size[WIDTH]), cell_size, window, WHITE)

    # Draw the vertices of the shortest path
    for vertex in shortest_path:
        draw_cell(index_to_coords(vertex, maze_size[WIDTH]), cell_size, window, LIGHT_RED)
    
    # Draw the entrance and the exit, where the entrance is green and the exit is red. The entrance is 0, 0 and the exit is maze_width - 1, maze_height - 1.
    draw_cell([0, 0], cell_size, window, (100, 255, 100))
    draw_cell([maze_size[0] - 1, maze_size[1] - 1], cell_size, window, (100, 100, 255))