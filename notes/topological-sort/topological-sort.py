from typing import List
from collections import deque


def topologicalSort(graph: List[List[int]]) -> List[int]:
    size = len(graph)
    visited = [False] * size
    result = deque()

    for v in range(1, size + 1):
        if not visited[v]: dfs(v, graph, visited, result)

    return [*result]


def dfs(v: int,
        graph : List[List[int]],
        visited : List[int],
        result : deque
    ):

    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, result)
    result.appendleft(v)
