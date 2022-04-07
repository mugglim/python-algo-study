import heapq
from typing import List
INF = int(1e10)

def reverseGraph(graph:List[List[int]]) -> List[List[int]]:
    n = len(graph)
    result = [[] for _ in range(n)]

    for vertex in range(1,n):
        for neighbor, cost in graph[vertex]:
            result[neighbor].append([vertex,cost])

    return result


def reversedDijkstra(graph:List[List[int]], s:int) -> List[List[int]]:
    size = len(graph)
    costs = [INF] * size
    costs[s] = 0
    minHeap = [(0, s)]
    reversedGraph = reverseGraph(graph)

    while minHeap:
        cost, vertex = heapq.heappop(minHeap)

        if costs[vertex] < cost: continue

        for nextVertex, nextCost in reversedGraph[vertex]:
            newCost = cost + nextCost

            if newCost < costs[nextVertex]:
                heapq.heappush(minHeap, (newCost, nextVertex))
                costs[nextVertex] = newCost

    return costs[1:]
