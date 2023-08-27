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

# This addresses challenge 15: The 14-15 puzzle

# All code in this file is authentically mine.
# If any system flags it as plagiarized, it is possibly due to an older version of this file,
# located at https://github.com/lochyj/School-Projects/blob/main/Data%20Science/Challenges/30min-challenge.py
# being in the public domain[1] for an extended period of time, around 6 months
# [1] on the internet, easily scraped by a crawler employed by an anti plagiarism company

# Some improvements that could be made to the AT3-1 assignment:

# For the more experienced programmer, possibly add an extract form the recent AIO.
# question 2 was quite interesting.
# TODO: add it here

# --------|
# Imports |
# --------|

import pygame
import random
from time import sleep

# ----------|
# Constants |
# ----------|

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

CELLS_WIDE = 4
CELLS_HIGH = 4

# what does `//` mean? `//`, opposed to `/` floors the result to a whole number after the division
# https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
# Source: https://www.w3schools.com/python/python_operators.asp
# E.G:
# import math
# math.floor(x / y)
# vs
# x // y
# Yes, I know it makes the program less readable, but in the long run it makes it cleaner and easier to follow.
CELL_WIDTH = WINDOW_WIDTH // CELLS_WIDE
CELL_HEIGHT = WINDOW_HEIGHT // CELLS_HIGH

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

screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

screen.fill(WHITE)

# TODO: is this on every system??
font = pygame.font.Font('freesansbold.ttf', 32)

pygame.display.set_caption("Lachlan Jowett's 14-15 Puzzle")

# ------------|
# Definitions |
# ------------|

gameGrid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, BLANK_CELL],
]

winningGrid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, BLANK_CELL]
]

# TODO: this doesn't work properly...
rand_nums = [[i + 1, i + 2, i + 3, i + 4] for i in range(0, TOTAL_CELLS, CELLS_WIDE)]

# this works but its silly and I hate it
random.shuffle(rand_nums)

running = True

# -----------------|
# Helper functions |
# -----------------|

def drawGrid():
    # This will actually be doubled? TODO: check if it is 2 px or 1 px wide...
    CELL_BORDER_WIDTH = 1 #px

    for cell_x in range(0, WINDOW_WIDTH, CELL_WIDTH):
        for cell_y in range(0, WINDOW_HEIGHT, CELL_WIDTH):
            cell_border = pygame.Rect(cell_x, cell_y, CELL_WIDTH, CELL_WIDTH)
            pygame.draw.rect(screen, BLACK, cell_border, CELL_BORDER_WIDTH)

def isWinning():
    if gameGrid == winningGrid:
        return True

    return False

def centreTextToCell(cell_row, cell_column):
    # TODO: This sucks, improve it. It works tho.
    return (cell_row * WINDOW_WIDTH // 4 + WINDOW_WIDTH // 8, cell_column * (WINDOW_WIDTH // 4) + WINDOW_WIDTH // 8) # We need to return a tuple, look for the function call to see why...

def drawGridElements():
    # i really dont like this nested for loop with the range(len(gameGrid)) stuff, try to simplify it
    for row in range(len(gameGrid)):
        for column in range(len(gameGrid[row])):
            if (gameGrid[row][column] == None):
                continue

            # What even is this?

            # font.render(<text to render>, <do we want anti aliasing, true / false>, <text colour>, <background colour>
            cellNumber = font.render(str(gameGrid[row][column]), True, BLACK, WHITE)

            # This probably isn't a frame buffer but i'd like to think that it is.
            cellNumberFrameBuffer = cellNumber.get_rect()

            cellNumberFrameBuffer.center = centreTextToCell(row, column)
            # TODO: explain what blit does
            screen.blit(cellNumber, cellNumberFrameBuffer)

def mousePosToGridCell(mouse_position):
    # What even happened here?
    return [mouse_position[0] // (WINDOW_WIDTH // 4), mouse_position[1] // (WINDOW_WIDTH // 4)]

def moveGrid(mouse_position):
    mouse_x, mouse_y = mousePosToGridCell(mouse_position)

    if (gameGrid[mouse_x][mouse_y] == BLANK_CELL):
        return
    else:
        # Check if any of the adjacent grids are empty
        # TODO This is terrible...
        if (mouse_x - 1 >= 0 and gameGrid[mouse_x - 1][mouse_y] == BLANK_CELL):
            gameGrid[mouse_x - 1][mouse_y] = gameGrid[mouse_x][mouse_y]
            gameGrid[mouse_x][mouse_y] = BLANK_CELL
        elif (mouse_x + 1 <= 3 and gameGrid[mouse_x + 1][mouse_y] == BLANK_CELL):
            gameGrid[mouse_x + 1][mouse_y] = gameGrid[mouse_x][mouse_y]
            gameGrid[mouse_x][mouse_y] = BLANK_CELL
        elif (mouse_y - 1 >= 0 and gameGrid[mouse_x][mouse_y - 1] == BLANK_CELL):
            gameGrid[mouse_x][mouse_y - 1] = gameGrid[mouse_x][mouse_y]
            gameGrid[mouse_x][mouse_y] = BLANK_CELL
        elif (mouse_y + 1 <= 3 and gameGrid[mouse_x][mouse_y + 1] == BLANK_CELL):
            gameGrid[mouse_x][mouse_y + 1] = gameGrid[mouse_x][mouse_y]
            gameGrid[mouse_x][mouse_y] = BLANK_CELL

        # even if nothing is done, we still need to return nothing
        return

# -------------------------|
# Game setup and main loop |
# -------------------------|

# Fill game grid with random values. TODO: OPTIMIZE
for row in range(len(gameGrid)):
    for column in range(len(gameGrid[row])):
        if gameGrid[row][column] == BLANK_CELL:
            continue

        gameGrid[row][column] = rand_nums[row][column]

# Main loop!
while running:

    # 10ms delay between rendering frames + other overhead
    # Also, why does the python sleep function use seconds instead of ms unlike every other language in existence ever.
    sleep(0.01)

    # Clear the screen
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            moveGrid(pos)

    if isWinning():
        print("You won!")
        running = False

    drawGrid()
    drawGridElements()

    pygame.display.update()

# -----------------|
# Exiting sequence |
# -----------------|

pygame.quit()
quit()
