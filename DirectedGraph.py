from Graph import Graph


class DirectedGraph(Graph):
    def __init__(self):
        self.graph: dict[int, dict[int, float]] = {}
        self.n: int = 0

    def add_edge(self, u: int, v: int, weight: float = 1):
        self.graph.get(u, {})[v] = weight

    def remove_edge(self, u, v):
        del self.graph[u][v]

    def traverse(self, algorithm, source, destination):
        algorithm(self.graph, source, destination)
