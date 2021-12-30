import sys
import heapq
from typing import List
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dijkstra(board:List[List[int]]) -> int:
    n = len(board)
    costs = [[INF for _ in range(n)] for _ in range(n)]

    heap = [(0,0,0)]
    costs[0][0] = 0

    while heap:
        cost, y,x = heapq.heappop(heap)

        if costs[y][x] < cost: continue

        for k in range(4):
            ny,nx = y+dy[k], x+dx[k]
            if ny < 0 or ny >= n or nx < 0 or nx >= n: continue

            newCost = cost + 1 if board[ny][nx] == 0 else cost

            if newCost < costs[ny][nx]:
                costs[ny][nx] = newCost
                heapq.heappush(heap, (newCost, ny,nx))

    return costs[n-1][n-1]

n = int(input())
board = [list(map(int,list(input()))) for _ in range(n)]
print(dijkstra(board))