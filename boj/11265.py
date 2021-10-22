import sys
input = lambda:sys.stdin.readline().rstrip()
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
query = [list(map(int,input().split())) for _ in range(m)]

def floyd(graph):
    n = len(graph)
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

floyd(graph)

for q in query:
    a, b, c = q
    print('Enjoy other party' if graph[a-1][b-1] <= c else 'Stay here')