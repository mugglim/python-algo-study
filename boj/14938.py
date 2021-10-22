'''
수색 범위 : 최대 cost
- 수색범위는 한 번에 이동이 아닌, 경로를 이동할 때 마다 발생
- 각 지점에 최단거리로 이동이 필요.
'''

INF = int(1e10)
n,m,r = map(int,input().split())
itemList = list(map(int,input().split()))
graph = [[INF] * n for _ in range(n)]
ans = 0
for _ in range(r):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

for i in range(n): graph[i][i] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[b][k])


for i in range(n):
    cnt = sum([itemList[idx] if cost <= m else 0 for idx,cost in enumerate(graph[i])])
    ans = max(ans,cnt)

print(ans)

