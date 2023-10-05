import pygame
import math

def draw_cell(cell, cell_size, window, colour):
    cell_width = cell_size[0]
    cell_height = cell_size[1]

    x = cell[0]
    y = cell[1]

    pygame.draw.rect(window, colour, (x * cell_width * 2, y * cell_height * 2, cell_width, cell_height), 0)

def draw_edges(coordinates, cell_size, maze_size, window, colour):
    cell_width = cell_size[0]
    cell_height = cell_size[1]

    ax = coordinates[0] // maze_size[0]
    ay = coordinates[0] % maze_size[1]

    bx = coordinates[1] // maze_size[0]
    by = coordinates[1] % maze_size[1]

    dx = 0
    dy = 0

    if ax < bx:
        dx = 1
    elif ax > bx:
        dx = -1

    if ay < by:
        dy = 1
    elif ay > by:
        dy = -1

    pygame.draw.rect(window, colour, (ax * cell_width * 2 + cell_width * dx, ay * cell_height * 2 + cell_height * dy, cell_width, cell_height), 0)

# Draws the maze from the adjacency matrix.
def draw_maze(maze, cell_size, maze_size, window, colour):

    for i in range(maze_size[1]):
        for j in range(maze_size[0]):
            draw_cell([j, i], cell_size, window, colour)

    for i, cell in enumerate(maze):
        for j, connected_cell in enumerate(cell):
            if connected_cell == 1:
                draw_edges([i, j], cell_size, maze_size, window, colour)

    # Draw the entrance and the exit, where the entrance is green and the exit is red. The entrance is 0, 0 and the exit is maze_width - 1, maze_height - 1.
    draw_cell([0, 0], cell_size, window, (100, 255, 100))
    draw_cell([maze_size[0] - 1, maze_size[1] - 1], cell_size, window, (100, 100, 255))

def draw_path(edges, maze_matrix, cell_size, maze_size, window, colour):

    maze_width = int(math.sqrt(len(edges[0])))
    maze_height = int(math.sqrt(len(edges)))

    for i, cell in enumerate(edges):
        for j, connected_cell in enumerate(cell):
            if connected_cell == 1:
                draw_edges([i, j], cell_size, maze_size, window, colour)

    # Draw the entrance and the exit, where the entrance is green and the exit is red. The entrance is 0, 0 and the exit is maze_width - 1, maze_height - 1.
    draw_cell([0, 0], cell_size, window, (100, 255, 100))
    draw_cell([maze_width - 1, maze_height - 1], cell_size, window, (100, 100, 255))