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


