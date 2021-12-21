## 목적
- 순서가 정해져 있는 작업을 위해, 작업 순서를 결정
- Ex) 선수과목, 스킬 트리

## 적용 조건
- 방향 그래프
- 사이클이 없는 그래프
- 두 조건을 만족하는 그래프를 **DAG(Directed Acyclic Graph)** 라고 한다.  


## 흐름
1. 그래프의 진입차수를 기록한다.
2. 진입차수가 0인 정점을 큐에 삽입한다.
    1. 큐에서 원소를 꺼내, 해당 정점에 연결 된 간선을 제거한다.
    2. 간선이 제거되어 진입차수가 0이면서, 방문하지 않은 정점이라면 큐에 삽입한다.
    3. 큐가 빌 때 까지 1~2 과정을 반복한다.

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
