from src.generator import generate_maze_adjacency_matrix, generate_maze_cell_matrix

def djikstras_algorithm(adjacency_matrix, start_node, end_node):

    # [dist, previous_node]
    dist = [[float("inf"), None] for _ in range(len(adjacency_matrix))]

    dist[start_node] = [0, None]

    ...

def generate_solved_adjacency_matrix(maze_adjacency_matrix, maze_size):
    adjacency_matrix = generate_maze_adjacency_matrix(maze_size[0], maze_size[1])

    return djikstras_algorithm(adjacency_matrix, 0, len(adjacency_matrix) - 1)

