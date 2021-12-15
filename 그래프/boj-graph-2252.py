import sys
from collections import deque
from typing import List
input = sys.stdin.readline


def dfs(v: int,
        graph : List[List[int]],
        visited : List[int],
        result : deque
    ) -> None:

    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, result)
    result.appendleft(v)


def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    result = deque()

    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)

    for v in range(1,n+1):
        if not visited[v]:
            dfs(v, graph, visited, result)

    print(*result)

if __name__ == "__main__":
    main()

