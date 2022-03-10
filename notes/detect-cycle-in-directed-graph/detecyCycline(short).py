def detect_cycle(graph):
    visited = {}
    cycle = {}

    def backtrack(node):
        if node in cycle or (node in visited and visited[node] == 1): return

        if node not in visited: visited[node] = -1
        if visited[node] == 0: cycle[node] = True

        visited[node] = 0
        for adj_node in graph[node]:
            backtrack(adj_node)
        visited[node] = 1

    for node in range(1, len(graph)):
        if cycle: return True
        backtrack(node)

    return False