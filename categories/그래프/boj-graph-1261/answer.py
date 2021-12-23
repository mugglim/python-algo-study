import sys
import heapq
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
INF = int(1e5)

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def isOutOfBounds(y,x): return y < 0 or y >= n or x < 0 or x >= m

def dijkstra(graph,start,end):
    n,m = len(graph), len(graph[0])
    costs = [[INF] * m for _ in range(n)]

    s_y, s_x = start
    e_y, e_x = end

    heap = [(0, s_y, s_x)]
    costs[s_y][s_x] = 0

    while heap:
        cost, y,x = heapq.heappop(heap)

        if costs[y][x] < cost:
            continue

        for k in range(4):
            ny,nx = y+dy[k], x+dx[k]

            if isOutOfBounds(ny,nx): continue

            newCost = cost + 1 if board[ny][nx] == 1 else cost

            if newCost < costs[ny][nx]:
                costs[ny][nx] = newCost
                heapq.heappush(heap, (newCost, ny,nx))

    return costs[e_y][e_x]

m,n = map(int, input().split())
board = [list(map(int,list(input()))) for _ in range(n)]
print(dijkstra(board, (0,0), (n-1,m-1)))