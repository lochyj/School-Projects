import pygame
import random

pygame.init()

# ----------|
# Constants |
# ----------|

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

TOTAL_CELLS = 16

# The value of the blank cell
BLANK_CELL = None

# -----|
# Init |
# -----|

CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
screen.fill(WHITE)

pygame.display.set_caption("14-15 Puzzle")

# ------------|
# Definitions |
# ------------|

font = pygame.font.Font('freesansbold.ttf', 32)

# Initialise game grid
gameGrid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, None],
]

winningGrid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, None]
]

# There is probably a better way of doing this
rand_nums = [[i + 1, i + 2, i + 3, i + 4] for i in range(1, TOTAL_CELLS, 4)]

random.shuffle(rand_nums)

running = True

# -----------------|
# Helper functions |
# -----------------|

def drawGrid():
    blockSize = WINDOW_WIDTH / 4    # Set the size of the grid block
    blockSize = int(blockSize)
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)

def isWinning():
    for i in range(len(gameGrid)):
        for j in range(len(gameGrid[i])):
            if gameGrid[i][j] != winningGrid[i][j]:
                return False
    return True

def centreTextToGrid(row, column):
    return (row * int(WINDOW_WIDTH / 4) + int(WINDOW_WIDTH / 8), column * int(WINDOW_WIDTH / 4) + int(WINDOW_WIDTH / 8))

def drawGridElements():
    for row in range(len(gameGrid)):
        for column in range(len(gameGrid[row])):
            if (gameGrid[row][column] == None):
                continue
            text = font.render(str(gameGrid[row][column]), True, BLACK, WHITE)
            textRect = text.get_rect()
            # Essentially what this is doing is centering the text in the middle of the grid block (i, j) 
            textRect.center = centreTextToGrid(row, column)
            screen.blit(text, textRect)

def mousePosToGridCell(mouse_position):
    return [int(mouse_position[0] / int(WINDOW_WIDTH / 4)), int(mouse_position[1] / int(WINDOW_WIDTH / 4))]

def moveGrid(mouse_position):
    x, y = mousePosToGridCell(mouse_position)

    if (gameGrid[x][y] == None):
        return  
    else:
        # Check if any of the adjacent grids are empty
        # TODO This is terrible...
        if (x - 1 >= 0 and gameGrid[x - 1][y] == None):
            gameGrid[x - 1][y] = gameGrid[x][y]
            gameGrid[x][y] = None
        elif (x + 1 <= 3 and gameGrid[x + 1][y] == None):
            gameGrid[x + 1][y] = gameGrid[x][y]
            gameGrid[x][y] = None
        elif (y - 1 >= 0 and gameGrid[x][y - 1] == None):
            gameGrid[x][y - 1] = gameGrid[x][y]
            gameGrid[x][y] = None
        elif (y + 1 <= 3 and gameGrid[x][y + 1] == None):
            gameGrid[x][y + 1] = gameGrid[x][y]
            gameGrid[x][y] = None
        else:
            return

# -------------------------|
# Game setup and main loop |
# -------------------------|

# Fill game grid with random values. OPTIMIZE
for row in range(len(gameGrid)):
    for column in range(len(gameGrid[row])):
        if gameGrid[row][column] == BLANK_CELL:
            continue

        else:
            gameGrid[row][column] = rand_nums[row][column]

while running:

    # Clear the screen
    screen.fill(WHITE)

    drawGrid()
    drawGridElements()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            moveGrid(pos)

    if isWinning():
        print("You won!")
        running = False

    pygame.display.update()

pygame.quit()
quit()
