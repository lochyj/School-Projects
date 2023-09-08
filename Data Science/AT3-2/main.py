# I dont really want to use pygame, however,
# there isn't really an alternative within python
# that I know of that is this simple.

import pygame

pygame.init()   # Here to stop errors with font initialization

from src.constants import *
from src.generator import generate_sudoku_grid, print_sudoku_grid
from src.display import *

def main():
    grid = generate_sudoku_grid(MEDIUM)
    # print_sudoku_grid(grid)

    window, gui_manager = initialise_window()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        draw_sudoku_grid(window, grid)
        draw_side_bar(window, gui_manager)

        pygame.display.update()
        window.fill(WHITE)


if __name__ == "__main__":
    main()