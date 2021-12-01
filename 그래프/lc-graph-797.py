class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        self.answer = []

        def dfs(curr, visited):
            if curr == n - 1:
                self.answer.append([*visited])
                return

            for _next in graph[curr]:
                if _next not in visited:
                    dfs(_next, [*visited, _next])
        dfs(0, [0])
        return self.answer

