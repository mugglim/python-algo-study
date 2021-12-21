from collections import deque
from typing import List

input = sys.stdin.readline

def getIndgreeList(graph: List[List[int]]) -> List[int]:
    size = len(graph)
    indegreeList = [0 for _ in range(size)]

    for v in range(1, size):
        for neightbor in graph[v]:
            indegreeList[neightbor] += 1

    return indegreeList

def topologicalSort(graph: List[List[int]]) -> List[int]:
    ans = []
    size = len(graph)
    indegreeList = getIndgreeList(graph)

    def isZeroIndegreeVetex(vertex:int) -> int: return indegreeList[vertex] == 0

    queue = deque([i for i in range(1, size) if isZeroIndegreeVetex(i)])

    while queue:
        vertex = queue.popleft()
        ans.append(vertex)

        for neighbor in graph[vertex]:
            indegreeList[neighbor] -= 1
            if isZeroIndegreeVetex(neighbor): queue.append(neighbor)

    return ans


