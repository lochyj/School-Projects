# My custom graph theory python library I made
# because my initial attempt was really slow and 
# used a really large adjacency matrix
class Graph:
    
    def __init__(self, directed: bool = False):
        self.directed = directed

        self.vertices: list[int] = []
        self.edges: list[int] = []

    

    def __str__(self):
        ... # TODO

    def get_vertices(self):
        return self.vertices

    # Connect vertex_a -> vertex_b if directed
    # else connect vertex_a <-> vertex_b
    # We dont check if its a self connection.
    def connect(self, vertex_a: int, vertex_b: int):
        if self.directed:
            self.edges.append((vertex_a, vertex_b))
        else:
            self.edges.append((vertex_a, vertex_b))
            self.edges.append((vertex_b, vertex_a))
    
    # Add a vertex to the graph with the id of the 
    # length of the vertices list.
    def add_vertex(self):
        self.vertices.append(len(self.vertices))
    
    def generate_graph(self, n_vertices):
        for i in range(n_vertices):
            self.add_vertex()

    def generate_adjacency_matrix(self):

        matrix = []

        for i in range(len(self.vertices)):
            matrix.append([])
            for j in range(len(self.vertices)):
                matrix[i].append(0)

        for edge in self.edges:
            matrix[edge[0]][edge[1]] = 1
        
        return matrix
    
    def from_adjacency_matrix(self, matrix):
        for i in range(len(matrix)):
            self.add_vertex()
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    self.connect(i, j)
    
    # TODO: make this less convoluted
    # TODO: make this not return itself if its no connected to itself
    def get_adjacent_vertices(self, vertex):
        if self.directed:
            return [edge[1] for edge in self.edges if edge[0] == vertex]
        
        return [edge[1] for edge in self.edges if edge[0] == vertex or edge[1] == vertex]
