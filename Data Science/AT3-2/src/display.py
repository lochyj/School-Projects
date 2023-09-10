import pygame
import pygame_gui

from src.constants import *

def initialise_window() -> None:
    pygame.display.set_caption("The Ultimate Sudoku")
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    window.fill(WHITE)

    gui_manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

    return [window, gui_manager]

def draw_sudoku_cell(grid, x, y, window):
    cell_top_left_x = x * CELL_WIDTH
    cell_top_left_y = y * CELL_HEIGHT

    cell_value = grid[x][y]

    if cell_value == None or cell_value == 0:
        cell_value = " "

    cell_text = font32.render(str(cell_value), True, BLACK)
    cell_text_rect = cell_text.get_rect()

    cell_text_rect.center = (
        cell_top_left_x + CELL_WIDTH // 2,
        cell_top_left_y + CELL_HEIGHT // 2
    )

    pygame.draw.rect(
        window,
        BLACK,
        (cell_top_left_x, cell_top_left_y,
            CELL_WIDTH, CELL_HEIGHT),
        1
    )

    window.blit(cell_text, cell_text_rect)

def draw_square(window, x, y):
    square_offset_x = x * 3 * CELL_WIDTH
    square_offset_y = y * 3 * CELL_HEIGHT

    pygame.draw.rect(
        window,
        BLACK,
        (square_offset_x, square_offset_y,
            CELL_WIDTH * 3, CELL_HEIGHT * 3),
        2
    )

def draw_sudoku_grid(window, grid: list[list[int]]) -> None:
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            draw_sudoku_cell(grid, x, y, window)

    for x in range(3):
        for y in range(3):
            draw_square(window, x, y)

# TODO
# Create the number selector on the right side of the screen
def draw_number_selector(window):
    offset_x = GAME_WIDTH
    offset_y = 0

    for row in range(3):
        for col in range(1, 4):

            number = col + (row * 3)

            number_text = font32.render(str(number), True, BLACK)

            number_text_rect = number_text.get_rect()

            number_text_rect.center = (
                offset_x + (col * CELL_WIDTH) - (CELL_WIDTH // 2),
                offset_y + (row * CELL_HEIGHT) + (CELL_HEIGHT // 2)
            )

            window.blit(number_text, number_text_rect)

    # Draw the squares around the numbers
    for row in range(3):
        for col in range(1, 4):
            square_offset_x = offset_x + (col * CELL_WIDTH) - CELL_WIDTH
            square_offset_y = offset_y + (row * CELL_HEIGHT)

            pygame.draw.rect(
                window,
                BLACK,
                (square_offset_x, square_offset_y,
                    CELL_WIDTH, CELL_HEIGHT),
                1
            )

def handle_number_selector_click(mouse_pos):
    offset_x = GAME_WIDTH
    offset_y = 0

    for row in range(3):
        for col in range(1, 4):
            square_offset_x = offset_x + (col * CELL_WIDTH) - CELL_WIDTH
            square_offset_y = offset_y + (row * CELL_HEIGHT)

            if square_offset_x <= mouse_pos[0] <= square_offset_x + CELL_WIDTH and \
                square_offset_y <= mouse_pos[1] <= square_offset_y + CELL_HEIGHT:
                return col + (row * 3)

    return None

def draw_moving_number(window, position, number):
    number_text = font32.render(str(number), True, BLACK)
    number_text_rect = number_text.get_rect()

    number_text_rect.center = (
        position[0],
        position[1]
    )

    window.blit(number_text, number_text_rect)

def draw_side_bar(window, gui_manager):
    draw_number_selector(window)

    # Draw the buttons and stuff here...