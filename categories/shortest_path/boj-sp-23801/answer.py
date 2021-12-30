import sys
import heapq
input = sys.stdin.readline

INF = int(3e5) * int(1e6) + 1

n,m = map(int,input().split())
ans = INF

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

x,z = map(int,input().split())
p = int(input())
layovers = list(map(int,input().split()))

def dijkstra(graph, s):
    heap = [(0,s)]
    costs = [INF] * len(graph)
    costs[s] = 0

    while heap:
        cost, vertex = heapq.heappop(heap)
        if costs[vertex] < cost: continue

        for adj, adjCost in graph[vertex]:
            newCost = cost + adjCost

            if newCost < costs[adj]:
                heapq.heappush(heap, (newCost, adj))
                costs[adj] = newCost

    return costs

xCosts = dijkstra(graph, x)
zCosts = dijkstra(graph, z)

for layover in layovers:
    if xCosts[layover] != INF and zCosts[layover] != INF:
        ans = min(ans, xCosts[layover] + zCosts[layover])

print(ans if ans != INF else -1)