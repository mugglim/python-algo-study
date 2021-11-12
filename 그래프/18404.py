from collections import deque
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

n,m = map(int,input().split())
x,y = map(lambda k:k-1,map(int,input().split()))

horseList = [map(lambda k:k-1,map(int,input().split())) for _ in range(m)]

queue = deque([(x,y)])
board = [[0] * n for _ in range(n)]
board[x][y] = 1


while queue:
    x,y = queue.popleft()
    for k in range(8):
        ny,nx = y+dy[k], x+dx[k]
`
        if 0 <= ny < n and 0 <= nx < n and board[nx][ny] == 0:
            board[nx][ny] = board[x][y] + 1
            queue.append((nx,ny))

result = [board[x][y] -1 for x,y in horseList]
print(*result)