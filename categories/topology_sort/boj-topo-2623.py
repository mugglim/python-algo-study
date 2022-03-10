from collections import deque

n,m = map(int,input().split())
singer_order_list = [list(map(int,input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
in_degree_list = [0] * (n+1)

for singer_order in singer_order_list:
    for i in range(1, len(singer_order)):
        # 그래프 관계 반영
        if i < len(singer_order) -1:
            node, adj_node = singer_order[i], singer_order[i+1]
            if adj_node not in graph[node]:
                graph[node].append(adj_node)
                in_degree_list[adj_node] += 1

queue = deque([i for i in range(1,n+1) if in_degree_list[i] == 0])
ans = []

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

def topology_sort(graph, in_degree_list):
    ans = []

    while queue:
        node = queue.popleft()
        ans.append(str(node))

        for adj_node in graph[node]:
            in_degree_list[adj_node] -= 1

            if in_degree_list[adj_node] == 0:
                queue.append(adj_node)

    return ans

if detect_cycle(graph):
    print(0)
else:
    print('\n'.join(topology_sort(graph, in_degree_list)))