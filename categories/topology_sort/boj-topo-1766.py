import heapq
import sys
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
indegree = [0 for i in range(n+1)]
adj_list = [[] for _ in range(n+1)]
answer = []

for _ in range(m):
    a,b = map(int,input().split())
    indegree[b] += 1
    adj_list[a].append(b)

min_heap = []

for node in range(1,n+1):
    if indegree[node] == 0:
        heapq.heappush(min_heap, node)

while min_heap:
    node = heapq.heappop(min_heap)
    answer.append(node)

    for adj_node in adj_list[node]:
        indegree[adj_node] -= 1

        if indegree[adj_node] == 0:
            heapq.heappush(min_heap, adj_node)

print(*answer)