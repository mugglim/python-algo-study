from collections import deque

def topology_sort(graph):
    ans = []
    size = len(graph)
    in_degree_list = [0 for i in range(size)]

    # init in_degree
    for node in range(1,size):
        for adj_node in graph[node]:
            in_degree_list[adj_node] += 1

    # insert node if in-degree of node is zero
    queue = deque([node for node in range(1, size) if in_degree_list[node] == 0])

    while queue:
        node = queue.popleft()
        ans.append(node)

        for adj_node in graph[node]:
            in_degree_list[adj_node] -= 1
            if in_degree_list[adj_node] == 0:
                queue.append(adj_node)

    return ans