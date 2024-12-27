
def DFS(graph: dict[int, list[int]], source: int, n: int):
    stack = [(source, 0)]
    dist = {source: 0}
    visited = [False] * n
    visited[source] = True

    while stack:
        curr = stack.pop(-1)
        print(curr)
        for x in graph.get(curr, []):
            if not visited[x]:
                visited[x] = True
                stack.append(x)
