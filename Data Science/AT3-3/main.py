import pygame

from pygame_gui import UI_BUTTON_PRESSED
from pygame_gui.elements import UIButton

from time import sleep

import resource, sys

# We need this because some inbuilt python functions use recursion
# for some reason and when we try to shuffle a list with a lot of
# elements it exceeds the recursion limit.
# It may also be a problem with my code... But I'm just gonna blame python. (Probably recursive my DFS)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

# ---------|
# Includes |
# ---------|

from src.generator import generate_maze
from src.draw_maze import draw_maze, draw_path, draw_cell
from src.solver import generate_solved_adjacency_matrix
from src.constants import *

# -----|
# Init |
# -----|

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

maze_size = [25, 25]

# The width and height of the maze "corridors"
vertex_size = [MAZE_WIDTH // (maze_size[0] * 2), MAZE_HEIGHT // (maze_size[1] * 2)]

maze = generate_maze(maze_size[0], maze_size[1])

solved_maze, matrix = generate_solved_adjacency_matrix(maze, maze_size)

# ----------|
# Main loop |
# ----------|

cursor_position = [0, 0]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            # If the cursor is in the maze
            if event.pos[0] < (vertex_size[0] * maze_size[0] * 2) and event.pos[1] < (vertex_size[1] * maze_size[1] * 2) and event.pos[0] > 0 and event.pos[1] > 0:
                cursor_position = [event.pos[0] // (vertex_size[0] * 2), event.pos[1] // (vertex_size[1] * 2)]


    draw_maze(maze, vertex_size, maze_size, window, (255, 255, 255))
    draw_path(solved_maze, matrix, vertex_size, maze_size, window, (200, 100, 100))

    pygame.draw.rect(window, (255, 255, 255), (MAZE_WIDTH, 0, WINDOW_WIDTH - MAZE_WIDTH, WINDOW_HEIGHT), 0)

    # Draw a cell at the position of the cursor...
    # This may draw it slightly outside of the maze, but that's fine.
    draw_cell(cursor_position, vertex_size, window, GREY)

    pygame.display.update()

    window.fill((0, 0, 0))

    # This is here to give the cpu a break :)
    sleep(0.01)

pygame.quit()
