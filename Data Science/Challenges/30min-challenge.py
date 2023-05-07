import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

CLOCK = pygame.time.Clock()
screen.fill(WHITE)

pygame.display.set_caption("14-15 Puzzle")

font = pygame.font.Font('freesansbold.ttf', 32)

# Initialise game grid
gameGrid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, None],
]

usedNums = []
for i in range(len(gameGrid)):
    for j in range(len(gameGrid[i])):
        if gameGrid[i][j] == None:
            continue
        else:
            # This can be improved
            tmp = random.randint(1, 15)
            while tmp in usedNums:
                tmp = random.randint(1, 15)
            gameGrid[i][j] = tmp
            usedNums.append(tmp)

gameGrid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12],
    [13, 14, 15, None]
]

def drawGrid():
    blockSize = WINDOW_WIDTH / 4    # Set the size of the grid block
    blockSize = int(blockSize)
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)

def isWinning():
    winningGrid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8], 
        [9, 10, 11, 12],
        [13, 14, 15, None]
    ]
    for i in range(len(gameGrid)):
        for j in range(len(gameGrid[i])):
            if gameGrid[i][j] != winningGrid[i][j]:
                return False
    return True

def printGrid():
    for i in range(len(gameGrid)):
        for j in range(len(gameGrid[i])):
            if (gameGrid[i][j] == None):
                continue
            text = font.render(str(gameGrid[i][j]), True, BLACK, WHITE)
            textRect = text.get_rect()
            # Essentially what this is doing is centering the text in the middle of the grid block (i, j) 
            textRect.center = (i * int(WINDOW_WIDTH / 4) + int(WINDOW_WIDTH / 8), j * int(WINDOW_WIDTH / 4) + int(WINDOW_WIDTH / 8))
            screen.blit(text, textRect)
            
def moveGrid(mousePos):
    getGridPos = lambda x: int(x / int(WINDOW_WIDTH / 4))
    x = getGridPos(mousePos[0])
    y = getGridPos(mousePos[1])

    if (gameGrid[x][y] == None):
        return  
    else:
        # check if any of the adjacent grids are empty
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

running = True
while running:
    drawGrid()
    printGrid()
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
    screen.fill(WHITE)

pygame.quit()
quit()
