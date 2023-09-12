# --------|
# Imports |
# --------|

import time
from time import sleep

import pygame

from pygame_gui import UI_BUTTON_PRESSED
from pygame_gui.elements import UIButton

pygame.init()   # Here to stop errors with font initialization

from src.constants import *
from src.generator import generate_sudoku_grid, if_number_is_valid
from src.display import *
from src.solver import remove_incorrect_numbers, find_random_next_move

# ----------------------------------------------|
# A few functions that dont need their own file |
# ----------------------------------------------|

def handle_number_placement(mouse_pos: list[int], selected_number: int, grid: list[list[int]]) -> None:
    grid_x = mouse_pos[0] // CELL_WIDTH
    grid_y = mouse_pos[1] // CELL_HEIGHT

    if grid_x > GRID_WIDTH - 1 or grid_y > GRID_HEIGHT - 1:
        return

    if grid[grid_x][grid_y] != EMPTY_CELL:
        return

    if if_number_is_valid(grid, grid_x, grid_y, selected_number):
        grid[grid_x][grid_y] = selected_number
    else:
        print("Invalid placement")

# If there are any empty cells, return false,
# because its not fully complete. Else return true
def is_grid_solved(grid):
    for row in grid:
        for cell in row:
            if cell == EMPTY_CELL:
                return False

    return True

current_difficulty = MEDIUM

def main():
    grid, completed_grid = generate_sudoku_grid(current_difficulty)

    window, gui_manager = initialise_window()

    # User interaction stuff
    mouse_pos = pygame.mouse.get_pos()
    drawing_moving_number = False
    selected_number = None
    # ---

    # Cheats
    cheats_enabled = False
    waiting_for_user_to_place_number = False
    placeholder_value = []

    toggle_cheats = UIButton(
        relative_rect=pygame.Rect(GAME_WIDTH + 10, 300, WINDOW_WIDTH - GAME_WIDTH - 20, 30),
        text="Toggle Cheats",
        manager=gui_manager
    )

    remove_incorrect_nums = UIButton(
        relative_rect=pygame.Rect(GAME_WIDTH + 10, 350, WINDOW_WIDTH - GAME_WIDTH - 20, 30),
        text="Remove Wrong Numbers",
        manager=gui_manager
    )

    regenerate = UIButton(
        relative_rect=pygame.Rect(GAME_WIDTH + 10, 400, WINDOW_WIDTH - GAME_WIDTH - 20, 30),
        text="Regenerate Grid",
        manager=gui_manager
    )

    # ---

    # High score stuff

    bestTime = None
    beginTime = 0
    endTime = 0

    # ---

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
                drawing_moving_number = False; selected_number = None

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos

            elif event.type == UI_BUTTON_PRESSED:
                if event.ui_element == toggle_cheats:
                    cheats_enabled = not cheats_enabled
                elif event.ui_element == remove_incorrect_nums:
                    remove_incorrect_numbers(grid, completed_grid)
                elif event.ui_element == regenerate:
                    grid, completed_grid = generate_sudoku_grid(current_difficulty)

            gui_manager.process_events(event)

        draw_sudoku_grid(window, grid)
        draw_side_bar(window, gui_manager)

        if drawing_moving_number and selected_number != None:
            draw_moving_number(window, mouse_pos, selected_number)

        if cheats_enabled:
            grid = remove_incorrect_numbers(grid, completed_grid)

            if not waiting_for_user_to_place_number:
                x, y, value = find_random_next_move(grid, completed_grid)

                while value == None:
                    x, y, value = find_random_next_move(grid, completed_grid)

                placeholder_value = [x, y, value]

                waiting_for_user_to_place_number = True

        if placeholder_value != [] and cheats_enabled:

            if grid[placeholder_value[0]][placeholder_value[1]] == placeholder_value[2]:
                waiting_for_user_to_place_number = False

            draw_placeholder_value(placeholder_value, window)


        if is_grid_solved(grid):
            grid, completed_grid = generate_sudoku_grid(current_difficulty)

        gui_manager.update(1 / 60)
        gui_manager.draw_ui(window)

        pygame.display.update()
        window.fill(WHITE)

        sleep(0.1)

if __name__ == "__main__":
    main()