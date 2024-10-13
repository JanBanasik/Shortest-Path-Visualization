from BFS import BFS
from DFS import DFS

graph = {0: [1, 3], 1: [2], 2: [4], 3: [2], 4: []}

#BFS(graph, 0, 5)
DFS(graph, 0, 5)
