import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
mi = lambda: list(map(int,input().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = mi()
hx,hy = map(lambda x: x-1, mi())
ex,ey = map(lambda x: x-1, mi())
board = [mi() for _ in range(n)]

visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
queue = deque([(hx, hy, 0, 0)])
visited[hx][hy][0] = True

def bfs():
    while queue:
        x,y, break_cnt, cost = queue.popleft()

        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if nx == ex and ny == ey: return cost + 1
            if board[nx][ny] == 1 and break_cnt == 1: continue

            new_break_cnt = break_cnt if board[nx][ny] == 0 else break_cnt + 1

            if not visited[nx][ny][new_break_cnt]:
                visited[nx][ny][new_break_cnt] = True
                queue.append((nx,ny,new_break_cnt,cost+1))

    return -1


print(bfs())
