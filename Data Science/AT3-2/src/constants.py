import pygame

# Sudoku grid size
GRID_WIDTH = 9
GRID_HEIGHT = 9

SQUARE_WIDTH = 3
SQUARE_HEIGHT = 3

# Difficulty levels
EASY = 38
MEDIUM = 45
HARD = 52

EMPTY_CELL = 0

# Window constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

GAME_WIDTH = 600
GAME_HEIGHT = 600

# This is kind of redundant and could be replaced with one CELL_SIZE constant
# but it looks clean so I'll keep it
CELL_WIDTH = GAME_WIDTH // GRID_WIDTH
CELL_HEIGHT = GAME_HEIGHT // GRID_HEIGHT

# The offset of the number pallette from the top of the screen to allow for a highscore.
PALLETTE_Y_OFFSET = 50

SHOULD_ANTIALIAS = True

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (255, 100, 110)

# Global fonts
font32 = pygame.font.SysFont("Arial", 32)
font24 = pygame.font.SysFont("Arial", 24)
font12 = pygame.font.SysFont("Arial", 12)
