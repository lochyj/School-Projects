from random import choice

from src.constants import *

# Does what it says on the tin. Removes incorrect numbers
# from grid in comparison to solved_grid
def remove_incorrect_numbers(grid, solved_grid):
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == EMPTY_CELL:
                continue

            if cell != solved_grid[x][y]:
                grid[x][y] = EMPTY_CELL

    return grid

# This actually doesn't work properly. It returns None even when the grid has open positions.
# I made a simple hack the somewhat works in the main file. I ran out of energy to fix this...
def find_random_next_move(grid: list[list[int]], solved_grid: list[list[int]]) -> list[int, int, int] | None:

    # This one liner; iterates through all of the cells in `grid` and
    # for that cell, if it is empty, places the value of the corresponding
    # cell in `solved_grid` in the corresponding position in the
    # new matrix (unused_cells). If the cell is populated in `grid`, then `unused_cells`,
    # in the corresponding position is filled with None which will be removed
    unused_cells = [[[i, j, solved_grid[i][j] if grid[i][j] == EMPTY_CELL else None] for j in range(len(grid[i]))] for i in range(len(grid))]

    # Linearize the matrix to an array.
    linearized_cells = [cell for row in unused_cells for cell in row]

    # Removing the None values so they cannot be returned
    for i, val in enumerate(linearized_cells):
        if val[2] == None:
            _ = linearized_cells.pop(i)

    # If there aren't any results to return.
    if len(linearized_cells) == 0:
        return 0

    # Pretty simple random.choice(). Returns a random value in the list.
    # Might be interesting to look into the python random lib to see if they use
    # a good source of entropy or if they use a simple non-cryptographic generator like glibc's random.
    return choice(linearized_cells)

