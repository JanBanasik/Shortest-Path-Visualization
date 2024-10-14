from Graph import Graph


class UndirectedGraph(Graph):
    def __init__(self):
        self.graph: dict[int, dict[int, float]] = {}
        self.n: int = 0

    def add_edge(self, u: int, v: int, weight: float = 1):
        self.graph.get(u, {})[v] = weight
        self.graph.get(v, {})[u] = weight

    def remove_edge(self, u, v):
        del self.graph[u][v]
        del self.graph[v][u]

    def traverse(self, algorithm, source, destination):
        algorithm(self.graph, source, destination)
