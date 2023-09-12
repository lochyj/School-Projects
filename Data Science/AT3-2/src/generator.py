from random import shuffle

from src.constants import *

# Temporary debugging function
def print_sudoku_grid(grid: list[list[int]]):
    print(*grid)

# This function is used to fill a 3x3 square with numbers 1 - 9.
# When we generate the grid, we use this to create a partially filled sudoku grid
# that is solvable by the naive solver I wrote.
def fill_square(grid, row, col):
    shuffled_numbers = list(range(1, 10))

    # This shuffles in place and as such we
    # cannot call it when we initialise the list above
    shuffle(shuffled_numbers)

    for i in range(3):
        for j in range(3):

            # The cell index is
            cell_index = j + (i * 3)

            grid[row + i][col + j] = shuffled_numbers[cell_index]

def if_number_is_valid(grid, row, column, num):
    # Check if the number is already in the row or column
    if num in grid[row] or num in [grid[i][column] for i in range(9)]:
        return False

    # Check if the number is already in the "square"
    # (The 3x3 box that the (row, column) lies in)

    # A quick explanation. We want to find the top x and y position of the
    # square. To do that, we floor divide the coordinate by 3 (the width / height)
    # of the square to get the square position. But to convert it to a cell
    # position, we need to multiply it by 3 (the width / height).
    # I can probably just square_x, square_y = [floor(row), floor(column)].
    # I just dont feel like testing it.
    square_x = SQUARE_WIDTH * (row // SQUARE_WIDTH)
    square_y = SQUARE_HEIGHT * (column // SQUARE_HEIGHT)

    # Checking if the number provided is it the "square" (3x3 box)
    for i in range(square_x, square_x + SQUARE_WIDTH):
        for j in range(square_y, square_y + SQUARE_HEIGHT):
            if grid[i][j] == num:
                return False

    return True

# To fill the sudoku grid in this way, we must have it partially filled.
# In my previous naive attempt, I didn't do this and the grid always had
# missing positions and was unsolvable.

# The grid provided has the the X's filled with numbers from 1 - 9 in
# random positions.
# X 0 0
# 0 X 0
# 0 0 X
# This creates a grid that is 100% valid but one
# square wont interfere with the other two.
# This gives us an easy to create base that makes it easy to
# complete the grid with no errors.
def fill_partially_completed_sudoku_grid(grid):
    for row in range(9):
        for col in range(9):

            # Pretty self explanatory;
            # if the cell is filled, skip it.
            if grid[row][col] != EMPTY_CELL:
                continue

            for potential_number in range(1, 10):
                if not if_number_is_valid(grid, row, col, potential_number):
                    continue # Skip the number as it isn't valid

                grid[row][col] = potential_number
                if fill_partially_completed_sudoku_grid(grid):
                    return True

                # The number isn't going to work to create a
                # full sudoku grid. Remove it.
                grid[row][col] = EMPTY_CELL

            # There aren't any good potential numbers
            return False

    # The grid is complete. Lets go back down the call stack
    # and exit this mess...
    return True

# Just remove random cells. This may produce solvable grids
# (so they are solved to the same point as when the grid was generate).
# However, I dont really want to spend too much time working on it.
def remove_cells(grid, difficulty):
    shuffled_cells = [[row, column] for row in range(GRID_WIDTH) for column in range(GRID_HEIGHT)]
    shuffle(shuffled_cells)
    for _ in range(difficulty):
        # Remove it from the list so we dont try to remove it from the grid again
        row, column = shuffled_cells.pop()
        grid[row][column] = EMPTY_CELL

def generate_sudoku_grid(difficulty = MEDIUM):
    grid = [[EMPTY_CELL for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    full_grid = [[EMPTY_CELL for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    for i in range(0, GRID_WIDTH, SQUARE_WIDTH):
        fill_square(grid, i, i)

    fill_partially_completed_sudoku_grid(grid)

    # copy the currently full grid to the full_grid
    # before it has numbers removed
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            full_grid[x][y] = cell

    remove_cells(grid, difficulty)

    return [grid, full_grid]
