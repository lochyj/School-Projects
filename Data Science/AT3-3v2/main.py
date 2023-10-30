# ---------|
# Includes |
# ---------|

# ---------
# 3rd Party
# ---------

import os

import pygame

from pygame_gui.elements import UIButton, UILabel
from pygame_gui import UI_BUTTON_PRESSED

# ---------
# Home made
# ---------

from lib.math import *

from src.solver import sp_djikstras

from src.maze import generate_new_maze
from src.display import init_window, draw_maze, draw_cell
from src.constants import *

# -------------------|
# Vars and constants |
# -------------------|

# The [width, height] of the maze
maze_size = [10, 10]

# -----|
# Init |
# -----|

# ----------
# Misc setup
# ----------

pygame.init()

maze, shortest_path = generate_new_maze(maze_size=maze_size)

window, ui_manager = init_window(GAME_WINDOW[WIDTH], GAME_WINDOW[HEIGHT], os.path.dirname(__file__) + '/theme.json')

# This is the position of the little 
# grey square that follows your cursor
cursor_position = [0, 0]

# ---------
# GUI Setup
# ---------

# The offset of the sidebar to 
# the right of the screen
GUI_WIDTH_OFFSET = GAME_WINDOW[WIDTH] - GUI_WINDOW[WIDTH]

regenerate_button = UIButton(
    relative_rect=pygame.Rect((GUI_WIDTH_OFFSET + 10, 10), (180, 30)),
    text="Regenerate",
    manager=ui_manager
)

inc_button = UIButton(
    relative_rect=pygame.Rect((GUI_WIDTH_OFFSET + 10, 60), (180, 30)),
    text="+",
    manager=ui_manager
)

dec_button = UIButton(
    relative_rect=pygame.Rect((GUI_WIDTH_OFFSET + 10, 100), (180, 30)),
    text="-",
    manager=ui_manager
)

maze_size_label = UILabel(
    relative_rect=pygame.Rect((GUI_WIDTH_OFFSET + 10, 150), (180, 50)),
    text=f"{maze_size[WIDTH]} x {maze_size[HEIGHT]}",
    manager=ui_manager
)

# -----------------|
# Helper functions |
# -----------------|

# The helper functions below need to be in-scope of the vars of this file

# Handle all of the events pertaining
# to UI elements
def gui_event_handler(event):
    global maze, shortest_path

    if event.ui_element == inc_button:
        
        # Limit the minimum and maximum size of the maze to 3 and 50 respectively
        maze_size[WIDTH] = clamp(3, maze_size[WIDTH] + 1, 50)
        maze_size[HEIGHT] = clamp(3, maze_size[HEIGHT] + 1, 50)

        maze_size_label.set_text(f"{maze_size[WIDTH]} x {maze_size[HEIGHT]}")
        
        maze, shortest_path = generate_new_maze(maze_size=maze_size)
    
    elif event.ui_element == dec_button:

        # Limit the minimum and maximum size of the maze to 3 and 50 respectively
        maze_size[WIDTH] = clamp(3, maze_size[WIDTH] - 1, 50)
        maze_size[HEIGHT] = clamp(3, maze_size[HEIGHT] - 1, 50)

        maze_size_label.set_text(f"{maze_size[WIDTH]} x {maze_size[HEIGHT]}")
        
        maze, shortest_path = generate_new_maze(maze_size=maze_size)
    
    elif event.ui_element == regenerate_button:
        maze, shortest_path = generate_new_maze(maze_size=maze_size)

# Converts the cursors pixel position to a position in the maze
def get_maze_relative_position_from_cursor(mouse_position) -> list[int, int]:

    cell_size = [MAZE_WINDOW[WIDTH] / maze_size[WIDTH] / 2, MAZE_WINDOW[HEIGHT] / maze_size[HEIGHT] / 2]

    # Limit the position of the cursor to be within the maze,
    # this requites some dumb looking code shown below.
    # `(cell_size[0] * maze_size[0] * 2)` -> We multiply the maze 
    # size by 2 because we have ~2 cells per vertex.
    # We then multiply that by the vertex size to get the size of the maze in pixels.
    mouse_position[0] = clamp(0, mouse_position[0], (cell_size[0] * maze_size[0] * 2))
    mouse_position[1] = clamp(0, mouse_position[1], (cell_size[1] * maze_size[1] * 2))

    # Reduce the pixel position to an index in the maze matrix.
    return  [mouse_position[0] // (cell_size[0] * 2), mouse_position[1] // (cell_size[1] * 2)]

# ----------|
# Main loop |
# ----------|

def main(window, ui_manager):

    clock = pygame.time.Clock()

    while True:
        time_delta = clock.tick(60) / 1000.0

        # ------
        # Events
        #-------

        # The main pygame event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            elif event.type == pygame.MOUSEMOTION:
                global cursor_position
                cursor_position = get_maze_relative_position_from_cursor([event.pos[0], event.pos[1]])

            elif event.type == UI_BUTTON_PRESSED:
                gui_event_handler(event)

            # The ui manager neets to handle 
            # events pertaining to the ui
            ui_manager.process_events(event)

        # -------
        # Drawing
        # -------

        # Draw the maze now.
        draw_maze(maze, shortest_path, maze_size, window)

        # Draw the little cursor thingy
        draw_cell(
            cursor_position,
            [
                MAZE_WINDOW[WIDTH] / maze_size[WIDTH] / 2,
                MAZE_WINDOW[HEIGHT] / maze_size[HEIGHT] / 2
            ], 
            window, 
            GREY
        )

        # Draw the white side-panel that has
        # all of the gui on it
        pygame.draw.rect(
            window, 
            WHITE, 
            (
                MAZE_WINDOW[WIDTH], 
                0, 
                GAME_WINDOW[WIDTH] - MAZE_WINDOW[WIDTH], 
                GAME_WINDOW[HEIGHT]
            ), 
            0
        )
        
        # -------
        # Updates
        # -------

        ui_manager.update(time_delta)

        ui_manager.draw_ui(window)
        pygame.display.update()

        # Fill the window with black, the background colour
        window.fill(BLACK)

    

if __name__ == "__main__":
    main(window, ui_manager)
