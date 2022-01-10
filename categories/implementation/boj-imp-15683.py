import sys
from itertools import product
input = sys.stdin.readline

dy = [-1,0,1,0]
dx = [0,1,0,-1]
ans = 64
cctvCases = []
board = []

dirs = {
    1: [[0],[1],[2],[3]],
    2: [[0,2], [1,3]],
    3: [[0,1], [1,2], [2,3], [3,0]],
    4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5: [[0,1,2,3]]
}

def deepCopy2DList(arr):
    return [row[:] for row in arr]

def isOutOfBounds(y,x):
    return y < 0 or y >= n or x < 0 or x >= m

def isWallPoint(y,x):
    return board[y][x] == 6

def applyCCTVArea(y,x,direction, targetBoard):
    ny,nx = y+dy[direction], x+dx[direction]

    if isOutOfBounds(ny,nx) or isWallPoint(ny,nx): return
    if targetBoard[ny][nx] == 0: targetBoard[ny][nx] = -1
    applyCCTVArea(ny,nx,direction, targetBoard)

def countBlindSpot(targetBoard):
    return len([True for i in range(n) for j in range(m) if targetBoard[i][j] == 0])

n,m = map(int,input().split())

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] < 1 or row[j] > 5: continue

        cctvCase = [(i,j,direction) for direction in dirs[row[j]]]
        cctvCases.append(cctvCase)

    board.append(row)

tempBoard = deepCopy2DList(board)
productedCCTVCases = list(product(*cctvCases))

for cases in productedCCTVCases:
    for y,x,dirs in cases:
        for direction in dirs:
            applyCCTVArea(y,x,direction, tempBoard)

    ans = min(ans, countBlindSpot(tempBoard))
    tempBoard = deepCopy2DList(board)

print(ans)


