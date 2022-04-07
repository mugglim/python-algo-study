## 목적
- **방향그래프**에서 사이클 여부를 확인한다.

## 제한사항
- 그래프를 인접리스트 형식으로 구헌한다.

## 시간복잡도
- O(V+E)

## 흐름

생각은 간단하다. 정점 A의 이웃 정점 B가 trace(경로)에 포함되어 있다면 사이클이 확인 된 것이다.

1. 3가지의 set을 준비한다.
   - whiteSet : 방문하지 않은 정점
   - graySet : 방문 중인 정점
   - blackSet : 방문이 완료 된 정점
2. whietSet의 길이가 0일때 까지 다음의 과정을 반복한다.
    1. whiteSet에서 랜덤으로 하나의 정점 A를 선택한다.
    2. 정점 A에서 다음의 순서로 DFS를 진행한다.
        - 1.) 정점 A를 graySet으로 이동시킨다.
        - 2.1) 정점 A에 이웃 정점이 없다면 정점 A를 blackSet으로 이동시킨다.
        - 2.2) 정점 A에 이웃 정점이 있다면 다음의 조건을 확인한다.
            - 이웃 정점이 blackSet에 포함되어 있다 => 이미 방문한 노드 => 추가 탐색 X
            - 이웃 정점이 graySet에 포함되어 있다 => 방문 중인 노드가 이웃 => 사이클 발생
    3. DFS의 결과가 True이면, 사이클이 발생했으므로 2번의 과정을 종료한다.
3. 2번 과정에서 종료가 발생하지 않았으므로, 사이클이 발생하지 않았다.


## 코드

### Set 이용
```python
from typing import Set, Dict, List

def moveVetex(vertex:int, prevSet:Set[int], newSet:Set[int]) -> None:
    prevSet.remove(vertex)
    newSet.add(vertex)

class DirectedGraph:
    def __init__(self, graph: Dict[int, List[int]]):
        self.graph = graph

    def hasCycle(self) -> bool:
        whiteSet:Set[int] = set()
        graySet:Set[int] = set()
        blackSet:Set[int] = set()

        for vertex in self.graph:
            whiteSet.add(vertex)

        while len(whiteSet) > 0:
            vertex = next(iter(whiteSet))
            if self.dfs(vertex, whiteSet, graySet, blackSet): return True

        return False

    def dfs(self, vertex:int, whiteSet:Set[int], graySet:Set[int], blackSet:Set[int]) -> bool:
        moveVetex(vertex, whiteSet, graySet)

        for neighbor in self.graph[vertex]:

            if neighbor in blackSet: continue
            if neighbor in graySet: return True
            if self.dfs(neighbor, whiteSet, graySet, blackSet): return True

        moveVetex(vertex, graySet, blackSet)
        return False

```

### List
```python
from typing import Dict, List


class DirectedGraph:
    def __init__(self, graph: Dict[int, List[int]]):
        self.graph = graph

    def hasCycle(self) -> bool:
        # -1 : unvisited vertex
        # 0 : visiting vertex
        # 1 : visited vertex

        visited = [-1] * (len(graph) + 1)

        for vertex in graph:
            if visited[vertex] == -1:
                if self.dfs(vertex, visited): return True

        return False

    def dfs(self, vertex:int, visited:List[int]) -> bool:
        visited[vertex] = 0

        for neighbor in self.graph[vertex]:

            if visited[neighbor] == 1: continue
            if visited[neighbor] == 0: return True
            if self.dfs(neighbor, visited): return True

        visited[vertex] = 1
        return False
```

## 연습문제
- https://leetcode.com/problems/course-schedule/

## Ref.
- https://www.youtube.com/watch?v=rKQaZuoUR4M