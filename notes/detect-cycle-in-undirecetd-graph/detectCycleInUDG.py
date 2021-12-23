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

graph = [
    [1,2],
    [1,3],
    [2,3]
]

print(hasCycle(graph))
