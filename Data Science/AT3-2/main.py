# I dont really want to use pygame, however,
# there isn't really an alternative within python
# that I know of that is this simple.

import pygame

pygame.init()   # Here to stop errors with font initialization

from src.constants import *
from src.generator import generate_sudoku_grid, check_if_number_is_valid
from src.display import *

def handle_number_placement(mouse_pos, selected_number, grid):
    grid_x = mouse_pos[0] // CELL_WIDTH
    grid_y = mouse_pos[1] // CELL_HEIGHT

    if grid_x > GRID_WIDTH - 1 or grid_y > GRID_HEIGHT - 1:
        return

    if grid[grid_x][grid_y] != 0:
        return

    if check_if_number_is_valid(grid, grid_x, grid_y, selected_number):
        grid[grid_x][grid_y] = selected_number
    else:
        print("Invalid placement")
        #TODO warn the user that the placement is invalid

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
                if drawing_moving_number and selected_number != None:
                    handle_number_placement(mouse_pos, selected_number, grid)
                drawing_moving_number = False
                selected_number = None

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