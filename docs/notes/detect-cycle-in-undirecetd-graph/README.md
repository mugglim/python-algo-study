## 목적
- 무방향 그래프에서 사이클을 확인해보자

## 제한 사항
- 인접 리스트 형식으로 그래프를 구현

## 시간복잡도
O(logn)
## 흐름

union-find를 이용해 두 정점의 부모가 동일하다면 사이클로 판별하면 된다.

```text
    1
   /  \
  2 ㅡ 3
```

```text
vertex      find(x)    find(y)   isCycle    parent
init          -           -         -       [1,2,3]
(1,2)         1           2       false     [1,1,3]
(1,3)         1           3       false     [1,1,1]
(2,3)         1           1       True 
```

## 코드
```python
from typing import List

class DisjointSet:
    def __init__(self, n:int):
        self.parent:List[int] = [x for x in range(n+1)]

    def find(self, x:int) -> int:
        if self.parent[x] == x: return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x:int,y:int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY: return True

        if rootX > rootY: self.parent[rootX] = rootY
        else: self.parent[rootY] = rootX

        return False


def hasCycle(graph: List[List[int]]) -> bool:
    size = len(graph) + 1

    ds:DisjointSet = DisjointSet(size)

    for a,b in graph:
        if ds.union(a,b): return True

    return False
```

## 연습문제
- https://www.acmicpc.net/problem/20040
