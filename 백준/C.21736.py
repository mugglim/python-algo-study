from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
board = []
visited = [[False]*m for _ in range(n)]
start = []
ans = 0

for i in range(n):
    row = list(input())
    for j in range(m):
        if row[j] == "I":
            start = [i,j]
            break
    board.append(row)

q = deque([start])
while q:
    y,x = q.popleft()
    for i in range(4):
        ny,nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] in ["O","P"] and visited[ny][nx] == False:
                if board[ny][nx] == "P":
                    ans += 1
                visited[ny][nx] = True
                q.append([ny,nx])

print(ans if ans else "TT")
