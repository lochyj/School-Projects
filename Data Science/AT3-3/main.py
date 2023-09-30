import pygame
from time import sleep
import resource, sys

# We need this because some inbuilt python functions use recursion
# for some reason and when we try to shuffle a list with a lot of
# elements it exceeds the recursion limit.
# It may also be a problem with my code... But I'm just gonna blame python.
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

# ---------|
# Includes |
# ---------|

from src.generator import generate_maze
from src.draw_maze import draw_maze
from src.solver import generate_solved_adjacency_matrix
from src.constants import *

# -----|
# Init |
# -----|

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

maze_size = [20, 20]

node_size = [MAZE_WIDTH // (maze_size[0] * 2), MAZE_HEIGHT // (maze_size[1] * 2)]

maze = generate_maze(maze_size[0], maze_size[1])

solved_maze = generate_solved_adjacency_matrix(maze, maze_size)

# ----------|
# Main loop |
# ----------|

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    draw_maze(maze, node_size, maze_size, window, (0, 0, 0))
    draw_maze(solved_maze, [20, 20], maze_size, window, (100, 0, 0))

    pygame.display.update()

    window.fill((255, 255, 255))

    # This is here to give the cpu a break :)
    sleep(0.01)

pygame.quit()
