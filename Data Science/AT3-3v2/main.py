# ---------|
# Includes |
# ---------|

from lib.graph import Graph

from src.solver import SP_Djikstras

# -----|
# Init |
# -----|

# We expect an uninitialized graph
def prims(graph: Graph, start_vertex: int):
    msp = Graph()

    msp.add_vertex(start_vertex)

    edges = graph.get_adjacent_vertices(start_vertex)

    while len(graph.get_vertices()) > len(msp.get_vertices()):
        ...


test = Graph()

test.generate_graph(5)

test.connect(0, 1)
test.connect(1, 2)
test.connect(2, 3)
test.connect(3, 4)

print(SP_Djikstras(test, 0, 4))
