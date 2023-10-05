
# ---------|
# Includes |
# ---------|

from lib.graph import Graph
from lib.queue import Queue

# -----------------|
# Public functions |
# -----------------|

# Shortest path djikstras
# An implementation of djikstras algorithm adapted 
# from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
def SP_Djikstras(graph: Graph, start_vertex: int, target_vertex: int):
    dist: list[int] = []
    prev: list[int] = []

    Q = Queue()

    for v in graph.get_vertices():
        dist.append(float('inf'))
        prev.append(None)
        Q.enqueue(v)

    dist[start_vertex] = 0

    while not Q.is_empty():
        u = Q.dequeue_preserve()

        if target_vertex is not None and u == target_vertex:

            if prev[u] != None or u == start_vertex:
                
                S = [u]

                while True:
                    u = prev[u]

                    if u is None:
                        break

                    S.append(u)

                # Return the reversed path
                return S[::-1]

        Q.remove()

        for v in graph.get_adjacent_vertices(u):
            if v in Q.get_queue():
                alt = dist[u] + 1

                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return None