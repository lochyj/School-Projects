import random
from random import shuffle

GRID_WIDTH = 9
GRID_HEIGHT = 9

SQUARE_WIDTH = 3
SQUARE_HEIGHT = 3

gameGrid = [[0 for j in range(GRID_WIDTH)] for i in range(GRID_HEIGHT)]
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_sudoku_grid(grid):
    print(" ====== ===== ====== ")
    for row in grid:
        print("| ", end="")
        for cell in row:
            if cell == None:
                print("  ", end="")
                continue
            print(f"{cell} ", end="")
        print("|")
    print(" ====== ===== ====== ")


def get_random_unused_number(grid, row, col):
    usedNumbers = []

    for i in grid[row]:
        if i == 0:
            continue

        usedNumbers.append(i)

    for i in range(GRID_HEIGHT):
        if i == 0:
            continue

        usedNumbers.append(grid[i][col])

    # Get the square that the cell is in
    squareX = col // SQUARE_WIDTH
    squareY = row // SQUARE_HEIGHT

    for x in range(squareX * SQUARE_WIDTH, squareX * SQUARE_WIDTH + SQUARE_WIDTH):
        for y in range(squareY * SQUARE_HEIGHT, squareY * SQUARE_HEIGHT + SQUARE_HEIGHT):
            if x == col and y == row:
                continue

            usedNumbers.append(grid[y][x])

    unusedNumbers = [i for i in numberList if i not in usedNumbers]

    if len(unusedNumbers) == 0:
        return None

    return random.choice(unusedNumbers)

def check_squares(grid):
    for x in range(0, GRID_WIDTH, SQUARE_WIDTH):
        for y in range(0, GRID_HEIGHT, SQUARE_HEIGHT):
            square = []

            for i in range(SQUARE_HEIGHT):
                for j in range(SQUARE_WIDTH):
                    square.append(grid[y + i][x + j])

            if len(square) != len(set(square)):
                return False

    return True

def fill_holes(grid):
    ...
    # TODO: figure out why i need this...

def fill_sudoku_grid(grid):
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            grid[x][y] = get_random_unused_number(grid, x, y)

    # There is certainly a better way to do this

    if check_squares(grid):
        ... # fill holes
    else:
        # This is to prevent recursion errors
        while not check_squares(grid):
            grid = [[0 for j in range(GRID_WIDTH)] for i in range(GRID_HEIGHT)]
            for x, row in enumerate(grid):
                for y, cell in enumerate(row):
                    grid[x][y] = get_random_unused_number(grid, x, y)

fill_sudoku_grid(gameGrid)

print_sudoku_grid(gameGrid)
