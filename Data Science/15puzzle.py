import pygame

import constants

pygame.init()

screen = pygame.display.set_mode(size = (WINDOW_HEIGHT, WINDOW_WIDTH), vsync = True)

screen.fill(WHITE)

font = pygame.font.Font('freesansbold.ttf', 32)

pygame.display.set_caption("Lachlan Jowett's 14-15 Puzzle")

def quit_game():
    pygame.quit()
    exit()

def game_scene():
    ...

options_grid = []

def resize_grid(width: int, height: int) -> None:
    # I really dislike that i cannot get a reference to options_grid and pass it though the function.
    # I guess its gonna be a global var then
    global options_grid

    # This may be hard to understand...
    # Why its needed
    # https://docs.python.org/3/library/stdtypes.html#index-20
    options_grid = [[0 for j in width] for i in height]

def create_text_box(width: int, height: int, border: bool):
    box_rect = pygame.Rect(width, height)

    box_rect.fill(WHITE)

    if border:
        pygame.draw.rect(box_rect, BLACK, [0, 0, width, height], 1)

    return box_rect


def options_scene():
    PANEL_WIDTH = 600
    PANEL_HEIGHT = WINDOW_WIDTH

    OPTIONS_WIDTH = 200
    OPTIONS_HEIGHT = WINDOW_WIDTH

    screen.fill(WHITE)

    selections_panel = pygame.Surface((OPTIONS_WIDTH, OPTIONS_HEIGHT))
    grid_panel = pygame.Surface((PANEL_WIDTH, PANEL_HEIGHT))

    selections_panel.fill(WHITE)
    grid_panel.fill(WHITE)

    pygame.draw.rect(selections_panel, BLACK, [0, 0, OPTIONS_WIDTH, OPTIONS_HEIGHT], 1)
    pygame.draw.rect(grid_panel, BLACK, [0, 0, PANEL_WIDTH, PANEL_HEIGHT], 1)

    options_text = font.render("Selection panel", ANTIALIAS, BLACK)

    current_grid_width = 4
    current_grid_height = 4

    resize_grid(current_grid_width, current_grid_height)

    width_value = create_text_box(20, 20, True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:

            if

        selections_panel.blit(options_text, [OPTIONS_WIDTH / 2 - (options_text.get_width() / 2), 10])

        screen.blit(selections_panel, [WINDOW_WIDTH - OPTIONS_WIDTH, 0])
        screen.blit(grid_panel, [0, 0])

        pygame.display.update()

        screen.fill(WHITE)




def main_menu():
    begin = font.render("Begin", ANTIALIAS, BLACK)
    options = font.render("Options", ANTIALIAS, BLACK)
    quit = font.render("Quit", ANTIALIAS, BLACK)

    currently_selected_menu_option = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    currently_selected_menu_option = max(currently_selected_menu_option - 1, 0)
                elif event.key == pygame.K_DOWN:
                    currently_selected_menu_option = min(currently_selected_menu_option + 1, 2)
                elif event.key == pygame.K_RETURN:
                    match currently_selected_menu_option:
                        case 0:
                            game_scene()
                        case 1:
                            options_scene()
                        case 2:
                            quit_game()

        # This is terrible

        match currently_selected_menu_option:
            case 0:
                begin = font.render("Begin", ANTIALIAS, GREEN)
                options = font.render("Options", ANTIALIAS, BLACK)
                quit = font.render("Quit", ANTIALIAS, BLACK)
            case 1:
                options = font.render("Options", ANTIALIAS, GREEN)
                begin = font.render("Begin", ANTIALIAS, BLACK)
                quit = font.render("Quit", ANTIALIAS, BLACK)
            case 2:
                quit = font.render("Quit", ANTIALIAS, GREEN)
                begin = font.render("Begin", ANTIALIAS, BLACK)
                options = font.render("Options", ANTIALIAS, BLACK)

        screen.blit(begin, [WINDOW_WIDTH//2 - (begin.get_width() / 2), (WINDOW_HEIGHT // 2) / 3 * 1])
        screen.blit(options, [WINDOW_WIDTH//2 - (options.get_width() / 2), (WINDOW_HEIGHT // 2) / 3 * 2])
        screen.blit(quit, [WINDOW_WIDTH//2 - (quit.get_width() / 2), (WINDOW_HEIGHT // 2) / 3 * 3])

        pygame.display.update()

        screen.fill(WHITE)




main_menu()

