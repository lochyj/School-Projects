from lib.graph import Graph

# Weighted graph is an extension of the graph class, 
# except it has an extra weight value for each edge 
# and a few helper functions
class WeightedGraph(Graph):

    # Invalidate the regular connect method
    def connect(self, vertex_a: int, vertex_b: int):
        raise NotImplementedError("Weighted graphs require a weight")
        exit(1)

    # Connect vertex_a -> vertex_b if directed
    # else connect vertex_a <-> vertex_b
    # We dont check if its a self connection.
    def connect(self, vertex_a: int, vertex_b: int, weight: int):
        if self.directed:
            self.edges.append((vertex_a, vertex_b, weight))
        else:
            self.edges.append((vertex_a, vertex_b, weight))
            self.edges.append((vertex_b, vertex_a, weight))
    
    # Generates a graph from a given adjacency matrix
    # It gives each edge a length of infinity
    def from_adjacency_matrix(self, matrix):
        for i in range(len(matrix)):
            self.add_vertex()
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    self.connect(i, j, float("inf"))
