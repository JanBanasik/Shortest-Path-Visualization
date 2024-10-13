from collections import deque


def BFS(graph: dict[int, list[int]], source: int, n: int):
    q = deque([source])

    visited = [False] * n
    visited[source] = True

    while q:
        curr = q.popleft()

        print(curr)
        for x in graph.get(curr, []):
            if not visited[x]:
                visited[x] = True
                q.append(x)
