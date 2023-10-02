import pygame

import pygame_gui
from pygame_gui import UI_BUTTON_PRESSED
from pygame_gui.elements import UIButton, UILabel

from time import sleep

import resource, sys, os

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

# -----------------|
# Helper functions |
# -----------------|

# Required initializations for pygame and pygame_gui
def initialise_window() -> list:

    pygame.display.set_caption("aMazing Software")

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    window.fill(WHITE)

    # This may be a source of issue for you as `os.path.dirname(__file__) + '/theme.json'`
    # gets the path of the config file for me on linux but may not for you.
    gui_manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT), os.path.dirname(__file__) + '/theme.json')

    return [window, gui_manager]

def clamp(minimum: int, x: int, maximum: int) -> int:
    return max(minimum, min(x, maximum))

# -----|
# Init |
# -----|

pygame.init()

window, gui_manager = initialise_window()

maze_size = [7, 7]

# The width and height of the maze "corridors" / "cells" / "vertices" / "nodes"
# As you can see I dont really know what to call them.
vertex_size = [MAZE_WIDTH / (maze_size[0] * 2), MAZE_HEIGHT / (maze_size[1] * 2)]

maze = generate_maze(maze_size[0], maze_size[1])

solved_maze, matrix = generate_solved_adjacency_matrix(maze, maze_size)

# ----------|
# GUI Setup |
# ----------|

regenerate = UIButton(
    relative_rect=pygame.Rect(MAZE_WIDTH + 10, 350, WINDOW_WIDTH - MAZE_WIDTH - 20, 30),
    text="Regenerate Maze",
    manager=gui_manager
)

inc = UIButton(
    relative_rect=pygame.Rect(MAZE_WIDTH + 150, 450, 40, 40),
    text="+",
    manager=gui_manager
)

dec = UIButton(
    relative_rect=pygame.Rect(MAZE_WIDTH + 10, 450, 40, 40),
    text="-",
    manager=gui_manager
)

current_size = UILabel(
    relative_rect=pygame.Rect(MAZE_WIDTH + 10, 400, WINDOW_WIDTH - MAZE_WIDTH - 10, 30),
    text=f"Maze size: {maze_size[0]}x{maze_size[1]}",
    manager=gui_manager
)

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

        elif event.type == UI_BUTTON_PRESSED:
            if event.ui_element == regenerate:
                maze = generate_maze(maze_size[0], maze_size[1])
                solved_maze, matrix = generate_solved_adjacency_matrix(maze, maze_size)
            elif event.ui_element == inc:
                # I didn't know I could do this until now
                maze_size[0] = maze_size[1] = clamp(3, maze_size[0] + 1, 100)

                current_size.set_text(f"Maze size: {maze_size[0]}x{maze_size[1]}")

                vertex_size = [MAZE_WIDTH / (maze_size[0] * 2), MAZE_HEIGHT / (maze_size[1] * 2)]

                maze = generate_maze(maze_size[0], maze_size[1])
                solved_maze, matrix = generate_solved_adjacency_matrix(maze, maze_size)

            elif event.ui_element == dec:
                # I didn't know I could do this until now
                maze_size[0] = maze_size[1] = clamp(3, maze_size[0] - 1, 100)

                current_size.set_text(f"Maze size: {maze_size[0]}x{maze_size[1]}")

                vertex_size = [MAZE_WIDTH / (maze_size[0] * 2), MAZE_HEIGHT / (maze_size[1] * 2)]

                maze = generate_maze(maze_size[0], maze_size[1])
                solved_maze, matrix = generate_solved_adjacency_matrix(maze, maze_size)

        # The GUI manager takes events and I guess creates
        # a new event for UI_BUTTON_PRESSED if its a relevant event.
        gui_manager.process_events(event)


    draw_maze(maze, vertex_size, maze_size, window, (255, 255, 255))
    draw_path(solved_maze, matrix, vertex_size, maze_size, window, (200, 100, 100))

    pygame.draw.rect(window, (255, 255, 255), (MAZE_WIDTH, 0, WINDOW_WIDTH - MAZE_WIDTH, WINDOW_HEIGHT), 0)

    # Draw a cell at the position of the cursor...
    # This may draw it slightly outside of the maze, but that's fine.
    draw_cell(cursor_position, vertex_size, window, GREY)

    gui_manager.update(1 / 60)
    gui_manager.draw_ui(window)

    pygame.display.update()

    window.fill((0, 0, 0))

    # This is here to give the cpu a break :)
    sleep(0.01)

pygame.quit()
