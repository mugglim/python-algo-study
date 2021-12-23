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

