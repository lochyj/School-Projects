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

    mouse_pos = pygame.mouse.get_pos()
    drawing_moving_number = False
    selected_number = None


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing_moving_number = True
                selected_number = handle_number_selector_click(mouse_pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                drawing_moving_number = False

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos

        draw_sudoku_grid(window, grid)
        draw_side_bar(window, gui_manager)

        if drawing_moving_number and selected_number != None:
            draw_moving_number(window, mouse_pos, selected_number)

        pygame.display.update()
        window.fill(WHITE)


if __name__ == "__main__":
    main()