# ---------|
# Includes |
# ---------|

import pygame
import pygame_gui

# I dont know why my linter says this is never accessed. It clearly is.
from pygame_gui import UI_BUTTON_PRESSED
from pygame_gui.elements import UIButton, UILabel

from time import sleep

import resource, sys, os, inspect

# ----------------
# My code includes
# ----------------

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

    # We need to set the initial background colour early 
    # otherwise we get a flash of some other colour.
    window.fill(WHITE)

    # This may be a source of issue for you as `os.path.dirname(__file__) + '/theme.json'`
    # gets the path of the config file for me on linux but may not for you.
    # It is really annoying that python doesn't have this built in like gcc does.
    gui_manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT), os.path.dirname(__file__) + '/theme.json')

    # Lets hope and pray that this doesn't go out of scope 
    # later on and get removed because python is python.
    return [window, gui_manager]

# This clamps a value between the values minimum and maximum for x.
# This is needed because python doesnt have this for some reason... 
# Might an interesting weekend project I guess
def clamp(minimum: int, x: int, maximum: int) -> int:
    return max(minimum, min(x, maximum))

# -----|
# Init |
# -----|

# We need this because some inbuilt python functions use recursion
# for some reason and when we try to shuffle a list with a lot of
# elements it exceeds the recursion limit.
# It may also be a problem with my code... But I'm just gonna blame python. (Probably my recursive DFS)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

# Initialise pygame, pygame!
pygame.init()

window, gui_manager = initialise_window()

# If you want larger sizes, modify this directly as it 
# will work better than the buttons for values > 20.
# Please dont use non square mazes, it wont look very good.
maze_size = [7, 7]

# The cursor position in terms of the maze cells.
# e.g. [0, 0] is the top left cell.
cursor_position = [0, 0]

# The width and height of the maze "corridors" / "cells" / "vertices" / "nodes"
# As you can see I dont really know what to call them.
vertex_size = [MAZE_WIDTH / (maze_size[0] * 2), MAZE_HEIGHT / (maze_size[1] * 2)]

maze = generate_maze(maze_size[0], maze_size[1])

solved_maze, matrix = generate_solved_adjacency_matrix(maze, maze_size)

# ----------|
# GUI Setup |
# ----------|

# Some generic pygame-gui stuff
# I hate the layout of these libraries,
# some many magic numbers and stuff to 
# make the interface clean.

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

# More helper functions

# Even though there are out of scope variables in here, 
# we dont run this function until they are defined 
# and as such python wont complain.
# In reality, at least to my knowledge, this isn't a good idea,
# however, this isn't designed for production use of any kind.
def modify_maze_size(vector: int):

    match vector:
        case -1:
            # We want to decrease the size of the maze by 1
            maze_size[0] = maze_size[1] = clamp(3, maze_size[0] - 1, 100)

        case 1:
            # We want to increase the size of the maze by 1
            maze_size[0] = maze_size[1] = clamp(3, maze_size[0] + 1, 100)

        case _: # The default case if none of the above cases are satisfied
            try:
                raise ValueError(
                    f"\nSomething went terribly wrong at: {inspect.getframeinfo(inspect.currentframe()).lineno}\n"
                    f"Vector passes wasn't -1 or 1 it was: {vector}\n"
                    "This was probably a freak error and shouldn't happen again *fingers crossed*\n"
                    "Lets exit the program just incase..." # Python will insert the newline here so no need
                )
            except ValueError as err:
                print(err)
                exit(1) # Exit with an error

    # Get the global context for these variables 
    # *smh python I shouldn't have to do this when I define them in a global scope
    global current_size, vertex_size, maze, solved_maze, matrix

    current_size.set_text(f"Maze size: {maze_size[0]}x{maze_size[1]}")

    # We re-calculate the vertex size to fit with the new size. 
    # (maze_size[0] * 2) because we have for each vertex, ~2 cells because of 
    # the edges connecting them. (-1 for the final edge, although it isn't too bad)
    return [MAZE_WIDTH / (maze_size[0] * 2), MAZE_HEIGHT / (maze_size[1] * 2)]

def get_maze_relative_position_from_cursor(mouse_position) -> list[int, int]:
    # Limit the position of the cursor to be within the maze,
    # this requites some dumb looking code shown below.
    # `(vertex_size[0] * maze_size[0] * 2)` -> We multiply the maze 
    # size by 2 because we have ~2 cells per vertex.
    # We then multiply that by the vertex size to get the size of the maze in pixels.
    # We might be able to simply use MAZE_WIDTH and MAZE_HEIGHT here but I haven't tested it yet.
    mouse_position[0] = clamp(0, mouse_position[0], (vertex_size[0] * maze_size[0] * 2))
    mouse_position[1] = clamp(0, mouse_position[1], (vertex_size[1] * maze_size[1] * 2))

    # Reduce the pixel position to an index in the maze matrix.
    return  [event.pos[0] // (vertex_size[0] * 2), event.pos[1] // (vertex_size[1] * 2)]

# ----------|
# Main loop |
# ----------|

while True:

    # ------
    # Events
    # ------

    for event in pygame.event.get():

        if event == pygame.QUIT:
            pygame.quit()
            exit(0)

        elif event == pygame.MOUSEMOTION:
            cursor_position = get_maze_relative_position_from_cursor(event.pos)
            
        elif event == UI_BUTTON_PRESSED:

            # Because I dont like having too many nested match 
            # statements just use normal if statements here.

            if event.ui_element == regenerate:
                maze = generate_maze(maze_size[0], maze_size[1])
                solved_maze, matrix = generate_solved_adjacency_matrix(maze, maze_size)

            elif event.ui_element == inc:
                maze_size = modify_maze_size(1)
                
                # Re-generate the maze with the new size and solve it for us.
                maze = generate_maze(maze_size[0], maze_size[1])
                solved_maze, matrix = generate_solved_adjacency_matrix(maze, maze_size)


            elif event.ui_element == dec:
                maze_size = modify_maze_size(-1)
                
                # Re-generate the maze with the new size and solve it for us.
                maze = generate_maze(maze_size[0], maze_size[1])
                solved_maze, matrix = generate_solved_adjacency_matrix(maze, maze_size)
            
        # The GUI manager takes events and I guess creates
        # a new event for UI_BUTTON_PRESSED if its a relevant event.
        gui_manager.process_events(event)

    # -------
    # Drawing
    # -------

    draw_maze(maze, vertex_size, maze_size, window, WHITE)
    draw_path(solved_maze, matrix, vertex_size, maze_size, window, LIGHT_RED)
    
    # This is the side-bar on the right of the screen.
    pygame.draw.rect(window, WHITE, (MAZE_WIDTH, 0, WINDOW_WIDTH - MAZE_WIDTH, WINDOW_HEIGHT), 0)

    # Draw a cell at the position of the cursor...
    draw_cell(cursor_position, vertex_size, window, GREY)

    # ------
    # Update
    # ------

    gui_manager.update(1 / 60)  # 1 / 60 is 60fps
    gui_manager.draw_ui(window)

    pygame.display.update()

    window.fill(WHITE)

    # This is here to give the cpu a break :)
    sleep(0.01) # This gives the cpu 0.00666666666... seconds of calculations per frame (if we are aiming for 60fps)
    # There is most certainly better ways of doing this, I'm just over dealing with rtc's
