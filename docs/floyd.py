INT = int(1e10)

def floyd(graph):
    n = len(graph)

    dist = [[*graph[i]] for i in range(n)]

    for k in range(n):
        for a in range(n):
            for b in range(n):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    return dist
