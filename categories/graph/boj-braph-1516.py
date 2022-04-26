import heapq
import sys

input = lambda:sys.stdin.readline().rstrip()
MAX_NODE_SIZE = 501

adj_list = [[] for _ in range(MAX_NODE_SIZE)]
indegree = [0] * MAX_NODE_SIZE
costs = [0] * MAX_NODE_SIZE

n = int(input())

for node in range(1,n+1):
    info = list(map(int,input().split()))
    cost = info[0]
    prev_node_list = info[1:-1]
    costs[node] = cost

    # link node
    for prev_node in prev_node_list:
        indegree[node] += 1
        adj_list[prev_node].append(node)

heap = []

for node in range(1,n+1):
    if indegree[node] == 0:
        heapq.heappush(heap, (costs[node], node))

while heap:
    cost, node = heapq.heappop(heap)

    for adj_node in adj_list[node]:
        indegree[adj_node] -= 1

        if indegree[adj_node] == 0:
            costs[adj_node] += cost
            heapq.heappush(heap, (costs[adj_node], adj_node))

print('\n'.join(list(map(str,costs[1:n+1]))))
