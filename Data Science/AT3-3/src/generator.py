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

# ---

def visit_node(node, nodes):
    nodes[node[1]][node[0]] = 1
    return nodes

def was_node_visited(node, nodes):
    if nodes[node[1]][node[0]] == 1:
        return True

    return False

def get_adjacent_nodes(current_node, nodes, graph):
    width = graph[0]
    height = graph[1]

    adjacent_nodes = []

    # Check if the node is on the left edge of the graph.
    if current_node[0] != 0:
        adjacent_nodes.append([current_node[0] - 1, current_node[1]])

    # Check if the node is on the right edge of the graph.
    if current_node[0] != width - 1:
        adjacent_nodes.append([current_node[0] + 1, current_node[1]])

    # Check if the node is on the top edge of the graph.
    if current_node[1] != 0:
        adjacent_nodes.append([current_node[0], current_node[1] - 1])

    # Check if the node is on the bottom edge of the graph.
    if current_node[1] != height - 1:
        adjacent_nodes.append([current_node[0], current_node[1] + 1])

    random.shuffle(adjacent_nodes)

    return adjacent_nodes

# This needs the graph width and height...
def traverse_graph(from_node, to_node, edges, graph):
    width = graph[0]
    height = graph[1]

    #
    from_index = from_node[1] * width + from_node[0]
    to_index = to_node[1] * width + to_node[0]

    edges[from_index][to_index] = 1
    edges[to_index][from_index] = 1

    return edges

def print_maze(maze):
    for row in maze:
        print(str(row).replace("[", "").replace("]", ""))

# ----|
# DFS |
# ----|

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
    maze_nodes = generate_maze_cell_matrix(width, height)

    maze = dfs(maze_nodes, maze_edges, [0, 0], [width, height])

    #print_maze(maze)

    return maze

