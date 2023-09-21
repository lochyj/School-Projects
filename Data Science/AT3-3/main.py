import pygame
from time import sleep

from src.generator import generate_maze
from src.draw_maze import draw_maze

pygame.init()

window = pygame.display.set_mode((500, 500))

maze = generate_maze(15, 15)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    draw_maze(maze, [10, 10], window)

    pygame.display.update()

    window.fill((255, 255, 255))

    # This is here to give the cpu a break :)
    sleep(0.01)

pygame.quit()
