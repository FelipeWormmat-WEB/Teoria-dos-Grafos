class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))


# Criando um grafo com 4 vértices
g = Graph(4)

# Adicionando arestas
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

# Imprimindo a matriz de adjacência
g.print_adj_matrix()