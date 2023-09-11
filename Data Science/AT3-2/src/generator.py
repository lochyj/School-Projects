from random import shuffle

from src.constants import *

# I thought I was smart...
# What is this: https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python

# Fill in the diagonal 3x3 boxes with random numbers 1-9 to create a valid Sudoku grid
def fill_square(grid, row, col):
    nums = list(range(1, 10))
    shuffle(nums)
    index = 0
    for i in range(3):
        for j in range(3):
            grid[row + i][col + j] = nums[index]
            index += 1

def check_if_number_is_valid(grid, row, col, num):
    # Check if the number is already in the row or column
    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False

    # Check if the number is already in the 3x3 box
    square_x = SQUARE_WIDTH * (row // SQUARE_WIDTH)
    square_y = SQUARE_HEIGHT * (col // SQUARE_HEIGHT)

    for i in range(square_x, square_x + SQUARE_WIDTH):
        for j in range(square_y, square_y + SQUARE_HEIGHT):
            if grid[i][j] == num:
                return False

    return True

def fill_partially_completed_sudoku_grid(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if check_if_number_is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if fill_partially_completed_sudoku_grid(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def remove_cells(grid, difficulty):
    cells = [[row, column] for row in range(GRID_WIDTH) for column in range(GRID_HEIGHT)]
    shuffle(cells)
    for _ in range(difficulty):
        row, column = cells.pop()
        grid[row][column] = 0

def generate_sudoku_grid(difficulty=MEDIUM):
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    for i in range(0, GRID_WIDTH, SQUARE_WIDTH):
        fill_square(grid, i, i)

    fill_partially_completed_sudoku_grid(grid)

    remove_cells(grid, difficulty)

    return grid

if __name__ == "__main__":
    generate_sudoku_grid()
