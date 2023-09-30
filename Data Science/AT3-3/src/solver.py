from src.generator import generate_maze_adjacency_matrix, generate_maze_cell_matrix

def djikstras_algorithm(adjacency_matrix, start_node, end_node, maze_size):

    vertices = [[0 for _ in range(maze_size[0])] for _ in range(maze_size[1])]

    # All distances are 1. I refuse to elaborate on why.




def generate_solved_adjacency_matrix(maze_adjacency_matrix, maze_size):
    adjacency_matrix = generate_maze_adjacency_matrix(maze_size[0], maze_size[1])

    return djikstras_algorithm(adjacency_matrix, 0, len(adjacency_matrix) - 1, maze_size)

