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


graph = {
    1: [2],
    2: [3],
    3: [],
    4: [5],
    5: [6],
    6: [4]
}

dg = DirectedGraph(graph)

print(dg.hasCycle())