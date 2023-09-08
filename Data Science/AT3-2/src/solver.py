from random import choice

def solve_sudoku_grid(grid):
    ...

def get_unfilled_cells(grid, solved_grid):
    ...  #TODO Move from function below

# I'm sorry for this abomination
def find_random_next_move(grid: list[list[int]], solved_grid: list[list[int]]) -> list[int, int, int] | None:
    # Thick one liner
    unused_cells = [[[i, j, solved_grid[i][j] if grid[i][j] == 0 else None] for j in range(len(grid[i]))] for i in range(len(grid))]

    # Another thick one liner
    linearized_cells = [unused_cells[i][j] for i in range(len(unused_cells)) for j in range(len(unused_cells[i]))]

    # Removing the None values so they cannot be returned
    for i, val in enumerate(linearized_cells):
        if val == None:
            linearized_cells.pop(i)

    if len(linearized_cells) == 0:
        return None

    return choice(linearized_cells)
