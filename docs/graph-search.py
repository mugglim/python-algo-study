## bfs
from collections import deque

def bfs(graph, start_vertex):
    queue = deque([start_vertex])
    result = []
    visited = {}
    visited[start_vertex] = True
    result.append(start_vertex)

    while queue:
        curr = queue.popleft()
        for _next in graph[curr]:
            if _next not in visited:
                visited[_next] = True
                queue.append(_next)
                result.append(_next)

    return result

## dfs
def dfs(value, visited):
    for _next in graph[value]:
        # (1)
        if not in visited:
            visited.append(value)
            dfs(_next, visited)
            visited.pop()
        # (2)
        if  not in visited:
            dfs(_next, [*visited, _next])

# dfs(0, [])