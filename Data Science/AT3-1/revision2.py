import pygame

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200

GAME_WINDOW_WIDTH = 400
GAME_WINDOW_HEIGHT = 400

CELLS_WIDE = 4
CELLS_HIGH = 4

CELL_WIDTH = GAME_WINDOW_WIDTH // CELLS_WIDE
CELL_HEIGHT = GAME_WINDOW_HEIGHT // CELLS_HIGH

def draw_game_grid(width: int, height: int):
    CELL_BORDER_WIDTH = 1 #px

    # range(<begin value>, <end value>, <increment value>)
    for cell_x_position in range(0, GAME_WINDOW_WIDTH, CELL_WIDTH):
        for cell_y_position in range(0, GAME_WINDOW_WIDTH, CELL_WIDTH):

            cell_border_pygame_object = pygame.Rect(cell_x_position, cell_y_position, CELL_WIDTH, CELL_WIDTH)

            pygame.draw.rect(screen, BLACK, cell_border_pygame_object, CELL_BORDER_WIDTH)