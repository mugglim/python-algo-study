from collections import deque
n,m = map(int,input().split())
board = [list(map(int,list(input()))) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False] *m for _ in range(n)]
queue = deque([])


for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append([i,j,0])
            board[i][j] = 0
            visited[i][j] = True

while queue:
    y,x,cnt = queue.popleft()
    visited[y][x] = True

    for k in range(4):
        ny,nx = y+dy[k], x+dx[k]

        if 0 <= ny < n and 0 <= nx < m:
            if visited[ny][nx] == False or (board[ny][nx] != 0 and cnt + 1 < board[ny][nx]):
                queue.append([ny,nx,cnt+1])
                visited[ny][nx] = True
                board[ny][nx] = cnt + 1

for b in board: print(*b)
