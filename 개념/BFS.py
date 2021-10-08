from collections import deque


def bfs(graph, start_vertex):
    queue = deque([start_vertex])
    answer = []
    visited = {}
    visited[start_vertex] = True
    answer.append(start_vertex)

    while queue:
        curr = queue.popleft()
        for _next in graph[curr]:
            if _next not in visited:
                visited[_next] = True
                queue.append(_next)
                answer.append(_next)

    return answer
