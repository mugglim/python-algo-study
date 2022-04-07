from typing import Dict, List


class DirectedGraph:
    def __init__(self, graph: Dict[int, List[int]]):
        self.graph = graph

    def hasCycle(self) -> bool:
        # -1 : unvisited vertex
        # 0 : visiting vertex
        # 1 : visited vertex

        visited:Dict[int, int] = {v: -1 for v in graph}

        for v in visited:
            if visited[v] == -1:
                if self.dfs(v, visited): return True

        return False

    def dfs(self, vertex:int, visited:Dict[int,int]) -> bool:
        visited[vertex] = 0

        for neighbor in self.graph:

            if visited[neighbor] == 1: continue
            if visited[neighbor] == 0: return True
            if self.dfs(neighbor, visited): return True

        visited[vertex] = 1
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