## 목적
- N개의 정점을 가지는 방향그래프에서, 각 정점 `v_1, v_2, ... v_n-1`에서 동일한 도착 정점 `v_e` 까지의 최단 거리를 구하고자 한다.
- 단, `v_1, v_2, ... v_n-1` -> `v_e` 까지의 최단거리이며, `v_e` -> `v_1, v_2, ... v_n-1` 까지의 최단거리를 의미하지 않는다.

## 제한 사항
- 방향 그래프
- 동일한 도착 정점

## 시간복잡도
> O(V + ElogV)

## 흐름

1. 기존의 간선의 방향을 반전 시킨다. 
    - 양방향 그래프로 만드는 것과 동일. 
    - 출발 정점을 기준으로 정점 A --> B로 이동하는 비용이랑
    - 도착 정점을 기준으로 정점 B --> A로 이동하는 비용이랑 같을테니.. (헷갈리네요..😤)
2. 도착 정점을 기준으로 다익스트라 알고리즘을 수행한다.
    - 다익스트라 알고리즘은 도착 정점 뿐만 아니라, 모든 정점에 대하여 최단 시간을 보장한다.

## 코드

```python
import heapq
from typing import List
INF = int(1e10)

def reverseGraph(graph:List[List[int]]) -> List[List[int]]:
    n = len(graph)
    result = [[] for _ in range(n)]

    for vertex in range(1,n):
        for neighbor, cost in graph[vertex]:
            result[neighbor].append([vertex,cost])

    return result


def reversedDijkstra(graph:List[List[int]], s:int) -> List[List[int]]:
    size = len(graph)
    costs = [INF] * size
    costs[s] = 0
    minHeap = [(0, s)]
    reversedGraph = reverseGraph(graph)

    while minHeap:
        cost, vertex = heapq.heappop(minHeap)

        if costs[vertex] < cost: continue

        for nextVertex, nextCost in reversedGraph[vertex]:
            newCost = cost + nextCost

            if newCost < costs[nextVertex]:
                heapq.heappush(minHeap, (newCost, nextVertex))
                costs[nextVertex] = newCost

    return costs[1:]
```


## 연습문제
- https://www.acmicpc.net/problem/1238
- https://www.acmicpc.net/problem/17835

