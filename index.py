class Vertice:
    def __init__(self, id, peso=0):
        self.id = id
        self.peso = peso
        self.adjacentes = []


class Aresta:
    def __init__(self, v1, v2, peso=0):
        self.v1 = v1
        self.v2 = v2
        self.peso = peso


class Grafo:
    def __init__(self, dirigido=False):
        self.vertices = []
        self.arestas = []
        self.dirigido = dirigido

    def add_vertice(self, vertice):
        self.vertices.append(vertice)

    def add_aresta(self, aresta):
        self.arestas.append(aresta)

    def get_vertices(self):
        return self.vertices

    def get_arestas(self):
        return self.arestas

    def get_grau(self, vertice):
        return len(vertice.adjacentes)

    def get_grau_total(self):
        grau_total = 0
        for vertice in self.vertices:
            grau_total += self.get_grau(vertice)
        return grau_total

    def busca_em_largura(self, vertice_inicial):
        visitados = set()
        queue = [vertice_inicial]

        while queue:
            vertice = queue.pop(0)
            visitados.add(vertice)
            for adjacente in vertice.adjacentes:
                if adjacente not in visitados:
                    queue.append(adjacente)

        return visitados

    def busca_em_profundidade(self, vertice_inicial):
        visitados = set()
        stack = [vertice_inicial]

        while stack:
            vertice = stack.pop()
            visitados.add(vertice)
            for adjacente in vertice.adjacentes:
                if adjacente not in visitados:
                    stack.append(adjacente)

        return visitados


grafo = Grafo()


grafo.add_vertice(Vertice(1))
grafo.add_vertice(Vertice(2))
grafo.add_vertice(Vertice(3))


grafo.add_aresta(Aresta(1, 2, 10))
grafo.add_aresta(Aresta(1, 3, 20))
grafo.add_aresta(Aresta(2, 3, 30))


for vertice in grafo.vertices:
    print(vertice.id, grafo.get_grau(vertice))

# Imprime o grau total do grafo
print(grafo.get_grau_total())

# Realiza a busca em largura
busca_largura = grafo.busca_em_largura(grafo.vertices[0])
print(busca_largura)

# Realiza a busca em profundidade
busca_profundidade = grafo.busca_em_profundidade(grafo.vertices[0])
print(busca_profundidade)
