import pygame
import random
from operator import length_hint

pygame.init()

# ----------|
# Constants |
# ----------|

WIDTH = 1000
HEIGHT = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
PURPLE = (200, 0, 200)
YELLOW = (200, 200, 0)
ORANGE = (200, 100, 0)
CYAN = (0, 200, 200)

# ------|
# Setup |
# ------|

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(WHITE)
pygame.display.set_caption("Pentominoes")

font = pygame.font.Font('freesansbold.ttf', 32)

pentominoesList = [
    [
        "##",
        "#",
        "##",
    ],
    [
        " #",
        "###",
        " #",
    ],
    [
        " #",
        "####",
    ],
    [
        "#####",
    ],
    [
        "###",
        " ##",
    ],
    [
        "###",
        "  #",
        "  #",
    ],
    [
        "###",
        " #",
        " #",
    ],
    [
        "##",
        " ###",
    ],
    [
        " ##",
        "##",
        "#",
    ],
    [
        "####",
        "#",
    ],
    [
        "#",
        "###",
        "  #",
    ],
    [
        " #",
        "###",
        "  #",
    ],
]

# generate a different grayscale color from 50 to 200 for each pentominoe
colours = [
    (30, 30, 30),
    (45, 45, 45),
    (60, 60, 60),
    (75, 75, 75),
    (90, 90, 90),
    (100, 100, 100),
    (110, 110, 110),
    (120, 120, 120),
    (135, 135, 135),
    (150, 150, 150),
    (175, 175, 175),
    (200, 200, 200),
]

pentominoesObjects = []

# -----------------|
# Helper functions |
# -----------------|

def drawGrid():
    blockSize = WIDTH / 20    # Set the size of the grid block
    blockSize = int(blockSize)
    for x in range(0, WIDTH, blockSize):
        for y in range(0, int(HEIGHT / 2), blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)

def drawPentominoe(pentominoe, x, y, colour = ORANGE):
    for i in range(len(pentominoe)):
        for j in range(len(pentominoe[i])):
            if pentominoe[i][j] == "#":
                rect = pygame.Rect((x + j) * int(WIDTH / 20) + 1, (y + i) * int(HEIGHT / 6) + 1, 48, 48)
                pygame.draw.rect(screen, colour, rect, 0)

def drawDraggingPentominoe(pentominoe, x, y, colour = ORANGE):
    for i in range(len(pentominoe)):
        for j in range(len(pentominoe[i])):
            if pentominoe[i][j] == "#":
                rect = pygame.Rect(x + j * int(WIDTH / 20), y + i * int(HEIGHT / 6), 48, 48)
                pygame.draw.rect(screen, colour, rect, 0)

running = True
dragging = False
draggingType = 0
draggingPos = [None, None]
while running:
    drawGrid()
    for pentominoe in pentominoesObjects:
        drawPentominoe(pentominoesList[pentominoe["index"]], pentominoe["x"], pentominoe["y"], colours[pentominoe["index"]])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                dragging = True
                draggingType = random.randint(0, 11)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                #tempx = int(pygame.mouse.get_pos()[0] - (pygame.mouse.get_pos()[0] % int(WIDTH / 20)) / int(WIDTH / 20))
                #tempy = int(pygame.mouse.get_pos()[1] - (pygame.mouse.get_pos()[1] % int(HEIGHT / 6)) / int(HEIGHT / 6))
                #pentHeight = pentominoesList[draggingType]
                #print(f"({pentHeight}, {tempy})")
                if pygame.mouse.get_pos()[1] > int(HEIGHT / 2):
                    ...
                #elif tempy + pentHeight > 3:
                #    ...
                else:
                    draggingPos = [ pygame.mouse.get_pos()[0] - (pygame.mouse.get_pos()[0] % int(WIDTH / 20)),
                                    pygame.mouse.get_pos()[1] - (pygame.mouse.get_pos()[1] % int(HEIGHT / 6))]


    if dragging:
        drawDraggingPentominoe(pentominoesList[draggingType], pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], colours[draggingType])

    if draggingPos[0] != None and draggingPos[1] != None:
        pentominoesObjects.append({"index": draggingType, "x": int(draggingPos[0] / int(WIDTH / 20)), "y": int(draggingPos[1] / int(HEIGHT / 6))})
        print(pentominoesObjects)
        draggingPos = [None, None]

    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()
quit()