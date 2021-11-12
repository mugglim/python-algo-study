# 우측 하단으로 이동하므로, 방향은 아래,오른쪽 방향만 고려하면 된다.
# BFS를 돌려 (N-1,m), (N,m-1)의 벽을 부순 개수의 최소를 고르면 될 것 같다.
# N 혹은 M 이 1일 수 있으므로, edge case를 고려해보자.
# 방문한 지점이라도, 새로 방문했을 때 부순 벽의 개수가 더 적다면, 새로 방문한 경우를 고려

from collections import deque
dy = [1,0]
dx = [0,1]
ans = int(1e10)

m,n  = map(int,input().split())
board = [list(map(int,list(input()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

queue = deque([(0,0)])

if n == 1 and m == 1:
    ans = 0
else:
    while queue:
        y,x = queue.popleft()
        for k in range(2):
            ny,nx = y+dy[k], x+dx[k]

            if ny == n - 1 and nx == m-1:
                ans = min(ans, -visited[y][x])

            if 0 <= ny < n and 0 <= nx < m:
                newDist = visited[y][x] - (1 if board[ny][nx] == 1 else 0)

                if not visited[ny][nx]:
                    queue.append((ny,nx))
                    visited[ny][nx] = newDist
                if visited[ny][nx] and visited[ny][nx] < newDist:
                    visited[ny][nx] = newDist



print(ans)