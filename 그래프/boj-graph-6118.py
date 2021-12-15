import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
queue = deque([(1,0)])
visited[1] = True
result = deque()

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

while queue:
    v, dist = queue.popleft()

    for nextV in graph[v]:
        if not visited[nextV]:
            visited[nextV] = True
            queue.append((nextV,dist + 1))
            if result and dist + 1 > result[0][1]: result = []
            result.append((nextV, dist + 1))


result = sorted(list(result), key=lambda x:x[0])

v, dist = result[0]
cnt = len(result)

print(v, dist ,cnt)