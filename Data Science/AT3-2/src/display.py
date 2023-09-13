import pygame
import pygame_gui

from src.constants import *

# Required initializations for pygame and pygame_gui
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

    # The cell may have a value of None. Idk why I haven't investigated.
    # If the cell == 0, then its a blank cell. So make it blank!
    if cell_value == None or cell_value == 0:
        cell_value = ' '

    cell_text = font32.render(str(cell_value), True, BLACK)
    cell_text_rect = cell_text.get_rect()

    # We use floor division here, it doesn't need it.
    # (Because CELL_WIDTH (And CELL_HEIGHT) is a literal of 66. When 66/2 it == 33. And when 66//2 it also == 33)
    # Although I dont want to change it just in case.
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

# Draws the "squares", the 3 cell x 3 cell box that
# visually separates the sudoku grid into 9 regions
def draw_square(window, x, y):
    square_offset_x = x * SQUARE_WIDTH * CELL_WIDTH
    square_offset_y = y * SQUARE_HEIGHT * CELL_HEIGHT

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

    for x in range(SQUARE_HEIGHT):
        for y in range(SQUARE_WIDTH):
            draw_square(window, x, y)

# TODO
# Create the number selector on the right side of the screen
def draw_number_selector(window):
    offset_x = GAME_WIDTH
    offset_y = PALLETTE_Y_OFFSET

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
    offset_y = PALLETTE_Y_OFFSET

    for row in range(3):
        for col in range(1, 4):
            square_offset_x = offset_x + (col * CELL_WIDTH) - CELL_WIDTH
            square_offset_y = offset_y + (row * CELL_HEIGHT)

            if square_offset_x <= mouse_pos[0] <= square_offset_x + CELL_WIDTH and \
               square_offset_y <= mouse_pos[1] <= square_offset_y + CELL_HEIGHT:
                return col + (row * 3)

    return None

# Used when the user has cheats enabled. It draws the red number that
# tells them what number to place and where to place it
def draw_placeholder_value(placeholder: list[int, int, int], window):

    # This function is basically the same as draw_sudoku_cell(),
    # however it has a different colour. It would be easy to add a
    # colour value and pass it to the function to reduce the amount of code.
    # However, it's here now and it works. No need to fix it.

    x, y, value = placeholder

    if value == None:
        return

    cell_top_left_x = x * CELL_WIDTH
    cell_top_left_y = y * CELL_HEIGHT

    cell_text = font32.render(str(value), True, LIGHT_BLUE)
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

# This is used when the user drags a number from the grid at the side onto the game grid
def draw_moving_number(window, position, number):
    number_text = font32.render(str(number), True, BLACK)
    number_text_rect = number_text.get_rect()

    number_text_rect.center = (
        position[0],
        position[1]
    )

    window.blit(number_text, number_text_rect)

# Reused functions from AT3-1

def draw_elapsed_time(time, window):

    size_text = font12.render(f"Time taken: {int((time))}s", SHOULD_ANTIALIAS, BLACK, WHITE)

    size_text_frame_buffer = size_text.get_rect()

    # Draw the text on the sidebar, 10px from the top
    size_text_frame_buffer.center = (((WINDOW_WIDTH - GAME_WIDTH) / 2) + GAME_WIDTH, 10)

    # Draw the text to the window
    window.blit(size_text, size_text_frame_buffer)

def draw_high_score(time, window):

    # If there isn't a high score
    if time == None:
        # Don't draw anything
        return

    size_text = font12.render(f"Best time: {int(time)}s", SHOULD_ANTIALIAS, BLACK, WHITE)

    size_text_frame_buffer = size_text.get_rect()

    # Draw the text on the sidebar, 50px from the top
    size_text_frame_buffer.center = ( ((WINDOW_WIDTH - GAME_WIDTH) / 2) + GAME_WIDTH, 25)

    # Draw the text to the window
    window.blit(size_text, size_text_frame_buffer)

# ---

# We draw the side bar. Mostly, the buttons are missing though.
# Self explanatory.
def draw_side_bar(window, time, best_time):
    draw_number_selector(window)

    draw_elapsed_time(time, window)
    draw_high_score(best_time, window)

