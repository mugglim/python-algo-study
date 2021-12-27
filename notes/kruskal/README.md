## 목적
- 크루스칼 알고리즘을 통해 최소 신장 트리를 구해보자.
- 용어
  - 신장 트리
    > 모든 정점을 연결하기 위한 간선의 최소 개수 : V-1 
    - 최소한의 간선의 개수로 모든 정점을 연결한 그래프 => 사이클이 발생하면 안 됨.
    <img src="./spanning-tree.png" width="500" height="300">
      - 출처 : [위키백과](https://ko.wikipedia.org/wiki/%EC%8B%A0%EC%9E%A5_%EB%B6%80%EB%B6%84_%EA%B7%B8%EB%9E%98%ED%94%84)
  - 최소 신장 트리
    - 간선의 가중치 합이 가장 작은 신장 트리

## 시간복잡도
> O(ElogE)

## 흐름
1. 간선을 비용에 따라 오름차순으로 정렬한다.
2. 정렬 된 간선을 확인하면서 **사이클이 발생하지 않은 경우에만** 최소 신장 트리에 포함시킨다.
    - 사이클 발생 여부는 유니온 파인드 자료구조를 통해 확인한다.

## 코드
```python
import heapq
from typing import List

class DisjointSet:
    def __init__(self, size):
        self.parents = [i for i in range(size+1)]

    def find(self, x:int) -> int:
        if self.parents[x] == x: return self.parents[x]

        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, rootX:int, rootY:int) -> None:
        if rootX < rootY: self.parents[rootY] = rootX
        else: self.parents[rootY] = rootX


def kruscal(v:int, edges:List[List[int]]) -> int:
    disjSet = DisjointSet(v)
    minHeap = []
    result = 0

    for a,b,cost in edges:
        heapq.heappush(minHeap, (cost, a, b))

    while minHeap:
        cost,x,y = heapq.heappop(minHeap)
        rootX, rootY = disjSet.find(x), disjSet.find(y)

        if rootX != rootY:
            result += cost
            disjSet.union(rootX, rootY)

    return result
```

## 연습문제
- https://www.acmicpc.net/problem/1197

## Ref.
- https://www.youtube.com/watch?v=Gj7s-Nrt1xE&t=314s
- https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html