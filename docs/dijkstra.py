import heapq
INF = int(1e10)

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

    return costs[end]
