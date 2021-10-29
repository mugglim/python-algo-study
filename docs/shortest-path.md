# Shortest-Path

### Dijkstra 
- [Reference](https://sungjk.github.io/2016/05/13/Dijkstra.html)
- `Big-O` : O(ElogV)
    - O(ElogE) = O(VlogE) (E << V<sup>2</sup>)
```python
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
```

### Floyd-Warshall
- `Big-O` : O(n<sup>3</sup>)

```python
def floyd(graph):
    n = len(graph)
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
```