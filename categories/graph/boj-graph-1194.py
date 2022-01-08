import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def isKeyPoint(y,x):
    return 97 <= ord(board[y][x]) <= 102

def isDoorPoint(y,x):
    return 65 <= ord(board[y][x]) <= 70

def isEndPoint(y,x):
    return board[y][x] == '1'

def isWallPoint(y,x):
    return board[y][x] == "#"

def isOutOfBounds(y,x):
    return y < 0 or y >= n or x < 0 or x >= m

def isVisitedPoint(ny,nx, keyBits):
    return visited[ny][nx][keyBits] == True

def hasKey(keyBits, key):
    return keyBits & (1 << (ord(key) - ord('A')))

def getAddedKey(keyBits, key):
    return keyBits | (1 << (ord(key) - ord('A')))

n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]

visited = [[[False] * (1 << 6) for _ in range(m)] for i in range(n)]
sy,sx = [[i,j] for i in range(n) for j in range(m) if board[i][j] == '0'][0]

def bfs():
    queue = deque([[sy, sx, 0, 0]])
    visited[sy][sx][0] = True

    while queue:
        y, x, keyBits, cost = queue.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if isOutOfBounds(ny, nx) or isWallPoint(ny,nx): continue
            if isDoorPoint(ny,nx) and not hasKey(keyBits, board[ny][nx]): continue
            if isEndPoint(ny,nx): return cost + 1

            # init new key bits
            newKeyBits = keyBits if not isKeyPoint(ny,nx) else getAddedKey(keyBits, board[ny][nx].upper())

            if not isVisitedPoint(ny,nx, newKeyBits):
                visited[ny][nx][newKeyBits] = True
                queue.append((ny,nx,newKeyBits, cost + 1))

    return -1

print(bfs())

