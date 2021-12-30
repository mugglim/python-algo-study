## 링크

https://leetcode.com/problems/course-schedule/

## 설명

수업 스케줄이 [[0,1], [1,0]] 이라고 가정해보면,  
1번 수업을 듣기 위해서는 0번 수업을 0번 수업을 듣기 위해서는 1번 수업을 들어야 하므로 스케줄을 소화하지 못한다.

수업 스케줄을 방향 그래프로 표현하여 사이클 여부를 판단하면 스케줄 소화 여부를 확인할 수 있다.

주의할 점은, `numCourses`가 1이고 `prerequisites` []인 경우도 정답으로 처리 된다.  
`prerequisites`은 그냥 수업을 듣기 위한 조건일 뿐 전체 수업을 의미하지는 않기 때문이다.

그래서 `numCourses`을 고려하지 않고 정답을 도출했다.


## 풀이
```python
from typing import List, Dict


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        visited = {}

        for s, e in prerequisites:
            if s not in graph: graph[s] = []
            if e not in graph: graph[e] = []
            if s not in visited: visited[s] = -1
            if e not in visited: visited[e] = -1

            graph[s].append(e)


        for v in visited:
            if visited[v] == -1:
                if self.dfs(graph, v, visited): return False

        return True

    def dfs(self, graph:Dict[int, List[int]], vertex:int, visited: Dict[int, int]) -> bool:
        visited[vertex] = 0

        for neighbor in graph[vertex]:

            if visited[neighbor] == 1: continue
            if visited[neighbor] == 0: return True
            if self.dfs(graph, neighbor, visited): return True

        visited[vertex] = 1
        return False
```


## 알게된 점
- 방향 그래프에서 순환 여부를 확인하는 방법

## 결과
|풀이|방식|시간|
|:---:|:---:|:--------:|
|1|사이클 여부 판단|96 ms| 
 
