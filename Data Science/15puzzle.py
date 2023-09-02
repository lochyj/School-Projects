import pygame
import pygame_gui
from pygame_gui import UI_BUTTON_PRESSED
from pygame_gui.elements import UIButton, UILabel

from constants import *

pygame.init()

screen = pygame.display.set_mode(size = (WINDOW_HEIGHT, WINDOW_WIDTH), vsync = True)
manager = pygame_gui.UIManager((WINDOW_HEIGHT, WINDOW_WIDTH))

screen.fill(WHITE)

font32 = pygame.font.Font('freesansbold.ttf', 32)
font24 = pygame.font.Font('freesansbold.ttf', 24)
font12 = pygame.font.Font('freesansbold.ttf', 12)

pygame.display.set_caption("Lachlan Jowett's 14-15 Puzzle")

def quit_game():
    pygame.quit()
    exit()

def clamp(number, smallest, largest):
    return max(smallest, min(number, largest))

options_grid = []
cell_width = 100
cell_height = 100

def draw_grid(surface):
    # This will actually be doubled? TODO: check if it is 2 px or 1 px wide...
    CELL_BORDER_WIDTH = 1 #px

    for cell_x_position in range(0, GAME_WIDTH, cell_width):
        for cell_y_position in range((WINDOW_HEIGHT - GAME_HEIGHT), WINDOW_HEIGHT, cell_height):

            cell_border_pygame_object = pygame.Rect(cell_x_position, cell_y_position, cell_width, cell_height)

            pygame.draw.rect(screen, BLACK, cell_border_pygame_object, CELL_BORDER_WIDTH)

def game_scene():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        draw_grid(screen)

        pygame.display.update()
        screen.fill(WHITE)


def resize_grid(width: int, height: int) -> None:
    # I really dislike that i cannot get a reference to options_grid and pass it though the function.
    # I guess its gonna be a global var then
    global options_grid

    # This may be hard to understand...
    # Why its needed
    # https://docs.python.org/3/library/stdtypes.html#index-20
    options_grid = [[0 for j in range(width)] for i in range(height)]


def options_scene():
    PANEL_WIDTH = 600
    PANEL_HEIGHT = WINDOW_HEIGHT

    OPTIONS_WIDTH = 200
    OPTIONS_HEIGHT = WINDOW_HEIGHT

    screen.fill(WHITE)

    options_panel = pygame_gui.elements.UIPanel(relative_rect = pygame.Rect(0, 0, OPTIONS_WIDTH, OPTIONS_HEIGHT), manager = manager)

    # create 3 buttons for cell type

    # 0 is blank, 1 is number 2 is inactive
    cell_type = 0

    blank_cell_button = UIButton(
        relative_rect = pygame.Rect(0, 0, 150, 150),
        text = "Blank Cell",
        manager = manager
    )

    number_cell_button = UIButton(
        relative_rect = pygame.Rect(0, OPTIONS_HEIGHT / 3, 150, 150),
        text = "Regular Cell",
        manager = manager
    )

    inactive_cell_button = UIButton(
        relative_rect = pygame.Rect(0, (OPTIONS_HEIGHT / 3) * 2, 150, 150),
        text = "Inactive Cell",
        manager = manager
    )

    cells_wide = 7
    cells_high = 7

    # set the colour of the grid_size_label UILabel to be black text

    # TODO

    grid_size_label = UILabel(
        relative_rect = pygame.Rect(PANEL_WIDTH + 15, WINDOW_HEIGHT - 300, 200, 100),
        text = f"Grid size: {cells_wide}x{cells_high}",
        manager = manager,
        object_id="#gsl"
    )

    increase_cells_wide_button = UIButton(
        relative_rect = pygame.Rect(PANEL_WIDTH + 50, WINDOW_HEIGHT - 100, 50, 50),
        text = "+ w",
        manager = manager
    )
    decrease_cells_wide_button = UIButton(
        relative_rect = pygame.Rect(PANEL_WIDTH + 125, WINDOW_HEIGHT - 200, 50, 50),
        text = "- w",
        manager = manager
    )

    increase_cells_high_button = UIButton(
        relative_rect = pygame.Rect(PANEL_WIDTH + 50, WINDOW_HEIGHT - 200, 50, 50),
        text = "+ h",
        manager = manager
    )
    decrease_cells_high_button = UIButton(
        relative_rect = pygame.Rect(PANEL_WIDTH + 125, WINDOW_HEIGHT - 100, 50, 50),
        text = "- h",
        manager = manager
    )


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == UI_BUTTON_PRESSED:
                # handle cell type buttons
                if event.ui_element == blank_cell_button:
                    blank_cell_button.focus()
                    cell_type = 0
                elif event.ui_element == number_cell_button:
                    blank_cell_button.focus()
                    cell_type = 1
                elif event.ui_element == inactive_cell_button:
                    blank_cell_button.focus()
                    cell_type = 2

                # handle grid size buttons
                elif event.ui_element == increase_cells_wide_button:
                    cells_wide = clamp(cells_wide + 1, 2, 14)


                elif event.ui_element == decrease_cells_wide_button:
                    cells_wide = clamp(cells_wide - 1, 2, 14)

                elif event.ui_element == increase_cells_high_button:
                    cells_high = clamp(cells_high + 1, 2, 14)

                elif event.ui_element == decrease_cells_high_button:
                    cells_high = clamp(cells_high - 1, 2, 14)

                grid_size_label.set_text(f"Grid size: {cells_wide}x{cells_high}")

            manager.process_events(event)

        manager.update(1 / 60)
        manager.draw_ui(screen)

        pygame.display.update()
        screen.fill(WHITE)



def main_menu():
    buttons_rect = pygame.Rect((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2), 200, 200)

    begin_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((WINDOW_WIDTH / 2) - (buttons_rect.width / 2), 200, buttons_rect.width, buttons_rect.height / 3.5), text = "Begin", manager = manager)
    options_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((WINDOW_WIDTH / 2) - (buttons_rect.width / 2), 300, buttons_rect.width, buttons_rect.height / 3.5), text = "Options", manager = manager)
    quit_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((WINDOW_WIDTH / 2) - (buttons_rect.width / 2), 400, buttons_rect.width, buttons_rect.height / 3.5), text = "Quit", manager = manager)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == UI_BUTTON_PRESSED:

                begin_button.kill()
                options_button.kill()
                quit_button.kill()

                if event.ui_element == begin_button:
                    game_scene()
                elif event.ui_element == options_button:
                    options_scene()
                elif event.ui_element == quit_button:
                    quit_game()

            manager.process_events(event)

        manager.update(1 / 60)
        manager.draw_ui(screen)

        pygame.display.update()
        screen.fill(WHITE)

main_menu()

