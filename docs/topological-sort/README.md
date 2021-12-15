## Goal
- 선후 관계가 정해져 있는 방향 그래프를 정렬해보자.
- **여러 가지 답이 존재할 수 있다.** 

## Code(DFS)
1. 방문하지 않는 정점에 대하여 DFS를 수행한다.
2. 이웃 정점이 존재하지 않아, 더 이상 탐색이 불가한 경우 탐색을 종료하고 결과에 정점을 반영한다.

```python
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
```

## Ref
- [위상 정렬](https://www.youtube.com/watch?v=m-Z19d2uS0w)
