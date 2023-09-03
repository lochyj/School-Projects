# ---------|
# Preamble |
# ---------|

# Contrary to the license in the base directory of the project, this file is licensed under the MIT License

# MIT License
# Copyright (c) 2023 Lachlan Jowett.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# -----|
# Info |
# -----|

# Prerequisites:
# - pygame
#   - Install with `pip install pygame`
# - pygame_gui
#   - Install with `pip install pygame_gui`

# This addresses challenge 15: The 14-15 puzzle

# The things I have added onto the challenge is a solvability check, which
# tests if the board is solvable and I also added resizing of the game board.

# I wanted to do more with this, however, I ran out of time to do it.
# Initially I wanted to create a solver to find the best move to make,
# but after a few hours decided it was too hard to do in a day so i moved onto
# making it solve the entire board and then play the moves back, which also took
# too long to make, so I settled with only resizing the game board.

# --------|
# Imports |
# --------|

import pygame
import random
from time import sleep
import pygame_gui
from pygame_gui import UI_BUTTON_PRESSED
from pygame_gui.elements import UIButton

# ----------|
# Constants |
# ----------|

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (128, 0, 0)

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 600

GAME_WINDOW_HEIGHT = 400
GAME_WINDOW_WIDTH = 400

SHOULD_ANTIALIAS = True

# Not a constant but its used to calculate constants
board_size = [4, 4]

# The following constants are here to make the code more readable.
# They give a meaningful value to the `magic` numbers scattered throughout the code

# what does `//` mean? `//`, opposed to `/` floors the result to a whole number after the division
# https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
# Source: https://www.w3schools.com/python/python_operators.asp
# E.G:
# import math
# math.floor(x / y)
# vs
# x // y
# Yes, I know it makes the program less readable, but in the long run it makes it cleaner and easier to follow.
CELL_WIDTH = GAME_WINDOW_WIDTH // board_size[0]
CELL_HEIGHT = GAME_WINDOW_HEIGHT // board_size[1]

HALF_CELL_WIDTH = CELL_WIDTH // 2
HALF_CELL_HEIGHT = CELL_HEIGHT // 2

TOTAL_CELLS = 16

# The value of a blank cell
BLANK_CELL = None


# -----|
# Init |
# -----|

# The obligatory pygame init
pygame.init()

# Initialize the clock for timing the user
CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode(size = (WINDOW_WIDTH, WINDOW_HEIGHT), vsync=True)

screen.fill(WHITE)

# TODO: is this on every system??
font32 = pygame.font.Font('freesansbold.ttf', 32)
font24 = pygame.font.Font('freesansbold.ttf', 24)
font12 = pygame.font.Font('freesansbold.ttf', 12)

pygame.display.set_caption("Lachlan Jowett's 15 Puzzle")

gui_manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

# ------------|
# Definitions |
# ------------|

# TODO: we should make the size of the gameGrid variable

gameGrid: list[list[int]] = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, BLANK_CELL],
]

winningGrid: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, BLANK_CELL]
]

isGameRunning = True

regenerate_button = UIButton(
    relative_rect=pygame.Rect(425, 30, 150, 30),
    text="Regenerate",
    manager=gui_manager
)

increase_board_size = UIButton(
    relative_rect=pygame.Rect(425, 110, 150, 30),
    text="+ board size",
    manager=gui_manager
)

decrease_board_size = UIButton(
    relative_rect=pygame.Rect(425, 150, 150, 30),
    text="- board size",
    manager=gui_manager
)

# -----------------|
# Helper functions |
# -----------------|

def regenerateGrid():

    randomGridNumbers = [i for i in range(1, TOTAL_CELLS)]

    random.shuffle(randomGridNumbers)

    # Fill the game grid with random values
    for cell_x, rows in enumerate(gameGrid):
        for cell_y, cell in enumerate(rows):
            if cell == BLANK_CELL:
                continue

            gameGrid[cell_x][cell_y] = randomGridNumbers.pop()

def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))

def grid_is_winning_grid(grid):
    if grid == winningGrid:
        return True

    return False

# Adapted from https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/

def getNumberOfInversions(array, N):

    number_of_inversions = 0

    for i in range(N * N - 1):
        for j in range(i + 1, N * N):
            if array[i] != BLANK_CELL and array[j] != BLANK_CELL and array[i] > array[j]:
                number_of_inversions += 1

    return number_of_inversions

def isGridSolvable():
    N = len(gameGrid)
    # this is pain. same as np flatten.
    flattened_grid = [item for row in gameGrid for item in row]

    number_of_inversions = getNumberOfInversions(flattened_grid, N)

    # TODO explain the magic bitwise operations going on here
    if N & 1:
        return not (number_of_inversions & 1)
    else:
        blank_cell_row = 0
        for i, row in enumerate(gameGrid):
            if BLANK_CELL in row:
                blank_cell_row = i
                break

        if blank_cell_row & 1:
            return not (number_of_inversions & 1)
        else:
            return number_of_inversions & 1

# ---------------

def drawSolvabilityText():

    if isGridSolvable():
        solvable_text = font24.render("Solvable", SHOULD_ANTIALIAS, GREEN, WHITE)
    else:
        solvable_text = font24.render("Unsolvable", SHOULD_ANTIALIAS, BLUE, WHITE)

    solvable_text_frame_buffer = solvable_text.get_rect()
    solvable_text_frame_buffer.center = ( ((WINDOW_WIDTH - GAME_WINDOW_WIDTH) / 2) + GAME_WINDOW_WIDTH, WINDOW_HEIGHT - 20)

    screen.blit(solvable_text, solvable_text_frame_buffer)

def drawBoardSizeText():

    size_text = font12.render(f"Board size: {board_size[0]}x{board_size[1]}", SHOULD_ANTIALIAS, BLACK, WHITE)

    size_text_frame_buffer = size_text.get_rect()
    size_text_frame_buffer.center = ( ((WINDOW_WIDTH - GAME_WINDOW_WIDTH) / 2) + GAME_WINDOW_WIDTH, 85)

    screen.blit(size_text, size_text_frame_buffer)

def drawGrid():
    # This will actually be doubled? TODO: check if it is 2 px or 1 px wide...
    CELL_BORDER_WIDTH = 1 #px

    # range(<begin value>, <end value>, <increment value>)
    for cell_x_position in range(0, GAME_WINDOW_WIDTH, CELL_WIDTH):
        for cell_y_position in range(0, GAME_WINDOW_HEIGHT, CELL_WIDTH):

            cell_border_pygame_object = pygame.Rect(cell_x_position, cell_y_position, CELL_WIDTH, CELL_WIDTH)

            pygame.draw.rect(screen, BLACK, cell_border_pygame_object, CELL_BORDER_WIDTH)

def get_centre_position_of_cell(cell_row, cell_column):
    cell_centre_x = (cell_row * CELL_WIDTH) + HALF_CELL_WIDTH
    cell_centre_y = (cell_column * CELL_HEIGHT) + HALF_CELL_HEIGHT

    return (cell_centre_x, cell_centre_y) # We need to return a tuple, look for the function call to see why...

# Draw the numbers into their respective cells
def drawGridElements():

    for row in range(len(gameGrid)):
        for column in range(len(gameGrid[row])):
            if (gameGrid[row][column] == None):
                continue

            if gameGrid[row][column] == winningGrid[column][row]:
                # font.render(<text to render>, <do we want anti aliasing, true / false>, <text colour>, <background colour>
                cell_number = font32.render(str(gameGrid[row][column]), True, GREEN, WHITE)
            else:
                cell_number = font32.render(str(gameGrid[row][column]), True, RED, WHITE)

            # This probably isn't a frame buffer but i'd like to think that it is.
            cell_number_frame_buffer = cell_number.get_rect()

            cell_number_frame_buffer.center = get_centre_position_of_cell(row, column)

            screen.blit(cell_number, cell_number_frame_buffer) # blit -> drawing to the screen

def mouse_position_to_grid_cell_position(mouse_position):
    # What even happened here?
    cell_row = mouse_position[0] // CELL_WIDTH
    cell_column = mouse_position[1] // CELL_HEIGHT
    return [cell_row, cell_column]

def move_grid_from_mouse_click(mouse_position):
    mouse_x, mouse_y = mouse_position_to_grid_cell_position(mouse_position)

    if mouse_x >= len(gameGrid[0]) or mouse_y >= len(gameGrid):
        return

    current_cell = gameGrid[mouse_x][mouse_y]


    if (current_cell == BLANK_CELL):
        return
    else:
        # Check if any of the adjacent grids are empty, if so,
        # move the square that was clicked on to that square and make the square that was clicked on blank

        # Unfortunately, we cannot get a reference to gameGrid[mouse_x][mouse_y] as current_cell
        # and we must directly change the value with gameGrid[mouse_x][mouse_y].

        if (mouse_x - 1 >= 0 and gameGrid[mouse_x - 1][mouse_y] == BLANK_CELL):
            gameGrid[mouse_x - 1][mouse_y] = current_cell
            gameGrid[mouse_x][mouse_y] = BLANK_CELL

        elif (mouse_x + 1 <= (board_size[0] - 1) and gameGrid[mouse_x + 1][mouse_y] == BLANK_CELL):
            gameGrid[mouse_x + 1][mouse_y] = current_cell
            gameGrid[mouse_x][mouse_y] = BLANK_CELL

        elif (mouse_y - 1 >= 0 and gameGrid[mouse_x][mouse_y - 1] == BLANK_CELL):
            gameGrid[mouse_x][mouse_y - 1] = current_cell
            gameGrid[mouse_x][mouse_y] = BLANK_CELL

        elif (mouse_y + 1 <= (board_size[0] - 1) and gameGrid[mouse_x][mouse_y + 1] == BLANK_CELL):
            gameGrid[mouse_x][mouse_y + 1] = current_cell
            gameGrid[mouse_x][mouse_y] = BLANK_CELL

# -------------------------|
# Game setup and main loop |
# -------------------------|

regenerateGrid()

# Main game loop
while isGameRunning:

    # 10ms delay between rendering frames + other overhead
    # This is to reduce unnecessary calculation and cpu usage
    # Also, why does the python sleep function use seconds instead of ms unlike every other language in existence ever.
    sleep(0.01)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            move_grid_from_mouse_click(mouse_position)

        elif event.type == UI_BUTTON_PRESSED:
            if event.ui_element == regenerate_button:
                regenerateGrid()
            elif event.ui_element == increase_board_size:
                board_size[0] = clamp(2, board_size[0] + 1, 7)
                board_size[1] = clamp(2, board_size[1] + 1, 7)
            elif event.ui_element == decrease_board_size:
                board_size[0] = clamp(2, board_size[0] - 1, 7)
                board_size[1] = clamp(2, board_size[1] - 1, 7)

        gui_manager.process_events(event)

    # This doesnt work for some reason
    if grid_is_winning_grid(gameGrid):
        print("You won!")
        isGameRunning = False

    drawGrid()
    drawGridElements()
    drawSolvabilityText()
    drawBoardSizeText()

    gui_manager.update(1 / 60)
    gui_manager.draw_ui(screen)

    pygame.display.update()

    # Clear the screen
    screen.fill(WHITE)


# -----------------|
# Exiting sequence |
# -----------------|

pygame.quit()
quit()