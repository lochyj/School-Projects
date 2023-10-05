import random

# -----------------|
# Helper functions |
# -----------------|

def generate_maze_adjacency_matrix(width, height):
    # This is an UNDIRECTED adjacency matrix (not like it will change the matrix init).
    # We dont need directions for a maze.
    maze_adjacency_matrix = [[0 for _ in range(width * height)] for _ in range(width * height)]

    return maze_adjacency_matrix

def generate_maze_cell_matrix(width, height):
    # The value in each cell basically represents if the node has been visited or not.
    maze_cell_matrix = [[0 for _ in range(width)] for _ in range(height)]

    return maze_cell_matrix

# Converts a set of coordinates to an index in the adjacency matrix.
def get_index_from_coordinates(coordinates, maze_size):
    return int(coordinates[1] * maze_size[0] + coordinates[0])

# Converts a set of coordinates to an index in the adjacency matrix.
def get_index_from_coordinates(coordinates, maze_size):
    return int(coordinates[1] * maze_size[0] + coordinates[0])

# Does what it says on the tin.
def visit_node(node, nodes):
    nodes[node[1]][node[0]] = 1
    return nodes

# Does what it says on the tin.
def was_node_visited(node, nodes):
    if nodes[node[1]][node[0]] == 1:
        return True

    return False

# For each surrounding node in the nodes graph, check if it has been visited.
# If not, return it.
def get_adjacent_nodes(current_node, nodes, graph):
    width = graph[0]
    height = graph[1]

    adjacent_nodes = []

    # Check if the node is:

    # On the left edge of the graph.
    if current_node[0] != 0:
        adjacent_nodes.append([current_node[0] - 1, current_node[1]])

    # On the right edge of the graph.
    if current_node[0] != width - 1:
        adjacent_nodes.append([current_node[0] + 1, current_node[1]])

    # On the top edge of the graph.
    if current_node[1] != 0:
        adjacent_nodes.append([current_node[0], current_node[1] - 1])

    # On the bottom edge of the graph.
    if current_node[1] != height - 1:
        adjacent_nodes.append([current_node[0], current_node[1] + 1])

    # Shuffle the list so we dont get the same path every time.
    random.shuffle(adjacent_nodes)

    return adjacent_nodes

# The basic traverse graph function, it uses a reference :angry: so it changes the original matrix.
def traverse_graph(from_node, to_node, edges, graph):

    from_index = get_index_from_coordinates(from_node, graph)
    to_index = get_index_from_coordinates(to_node, graph)

    edges[from_index][to_index] = 1
    edges[to_index][from_index] = 1

    return edges

# ----|
# DFS |
# ----|

# A basic recursive dfs algorithm.
def dfs(nodes, edges, current_node, graph):
    nodes = visit_node(current_node, nodes)

    for node in get_adjacent_nodes(current_node, nodes, graph):
        if was_node_visited(node, nodes):
            continue

        edges = traverse_graph(current_node, node, edges, graph)
        edges = dfs(nodes, edges, node, graph)

    return edges

# ------------------------|
# Public facing functions |
# ------------------------|

def generate_maze(width, height):
    maze_edges = generate_maze_adjacency_matrix(width, height)
    maze_vertices = generate_maze_cell_matrix(width, height)

    # [0,0] is the starting node.
    maze = dfs(maze_vertices, maze_edges, [0, 0], [width, height])

    return maze

