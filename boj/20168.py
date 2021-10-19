import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

n,m,a,b,c = map(int,input().split())
graph = [[] * n for _ in range(n)]
visited = [False] * n
answer = INF

for _ in range(m):
    x,y,z = map(int,input().split())

    graph[x-1].append([y-1,z])
    graph[y-1].append([x-1,z])



def dijkstra(graph,start,end):
    n = len(graph)
    costs = [INF] * n
    heap = [(0, start)]
    costs[start] = 0

    while heap:
        cost, currentVertex = heapq.heappop(heap)

        if costs[currentVertex] < cost:
            continue

        for l in graph[currentVertex]:
            nextVertex, nextCost = l
            newCost = cost + nextCost

            if newCost < costs[nextVertex]:
                costs[nextVertex] = newCost
                heapq.heappush(heap, (newCost, nextVertex))

    return costs

def dfs(node, maxCost, total):
    global answer, b,c

    # boundary condition
    if node == b-1:
        answer = min(answer, maxCost)
        return
    # recursive condition
    for l in graph[node]:
        nextNode, cost = l

        if not visited[nextNode] and total - cost >= 0:
            visited[nextNode] = True
            dfs(nextNode, max(maxCost, cost), total - cost)
            visited[nextNode] = False


costs = dijkstra(graph, a-1,b-1)
if costs[b-1] > c:
    print(-1)
else:
    # 이 시점부터 완탐 시작
    dfs(a-1, 0,c)
    print(answer if answer != INF else -1)

