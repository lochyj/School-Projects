import pygame
import math

# Draws the maze from the adjacency matrix.
def draw_maze(maze, cell_size, window):
    cell_width = cell_size[0]
    cell_height = cell_size[1]

    maze_width = int(math.sqrt(len(maze[0])))
    maze_height = int(math.sqrt(len(maze)))

    # Draw the outer walls of the maze

    # Top wall
    pygame.draw.line(window, (0, 0, 0), (0, 0), (maze_width * cell_width * 2, 0), 1)

    # Bottom wall
    pygame.draw.line(window, (0, 0, 0), (0, maze_height * cell_height * 2), (maze_width * cell_width * 2, maze_height * cell_height * 2), 1)

    # Left wall
    pygame.draw.line(window, (0, 0, 0), (0, 0), (0, maze_height * cell_height * 2), 1)

    # Right wall

    pygame.draw.line(window, (0, 0, 0), (maze_width * cell_width * 2, 0), (maze_width * cell_width * 2, maze_height * cell_height * 2), 1)


    # Draw the corridors connecting the cells from the adjacency matrix.
    for cell in maze:
        for connected_cell in cell:
            if connected_cell == 1:
                # Get the index of the connected cell.
                connected_cell_index = cell.index(connected_cell)

                # Get the x and y coordinates of the connected cell.
                connected_cell_x = connected_cell_index % maze_width
                connected_cell_y = connected_cell_index // maze_width

                cell_x = maze.index(cell) % maze_width
                cell_y = maze.index(cell) // maze_width

                # Draw the corridor.
                pygame.draw.line(window, (0, 0, 0), ((cell_x * cell_width) * 2 + cell_width, (cell_y * cell_height) * 2 + cell_height), ((connected_cell_x * cell_width) * 2 + cell_width, (connected_cell_y * cell_height) * 2 + cell_height), 1)