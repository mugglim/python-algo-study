import sys
input = sys.stdin.readline

MAX_SIZE = 9
dirs = [
    [0,-1],
    [0, 1],
    [-1,0],
    [1,0]
]


def isOutOfBounds(y,x): return y < 0 or y >= MAX_SIZE or x < 0 or x >= MAX_SIZE
def getUnselectedNum(trace):
    return [i for i in range(1,10) if i not in trace][0]

def dfs(y,x,k,v):
    if isOutOfBounds(y,x): return False
    if board[y][x] == v: return True

    ny,nx = y+dirs[k][0], x+dirs[k][1]
    return dfs(ny,nx,k,v)

def checkRow(y,v):
    for x in range(9):
        if board[y][x] == v: return True
    return False

def checkCol(x,v):
    for y in range(9):
        if board[y][x] == v: return True
    return False

def checkSquare(y,x,v):
    startY = y // 3 * 3
    startX = x // 3 * 3

    for i in range(startY, startY+3):
        for j in range(startX, startX+3):
            if board[i][j] == v: return True
    return False

def isDuplicate(y,x,v):
    if checkRow(y,v) or checkCol(x,v) or checkSquare(y,x,v): return True
    return False

def printBoard():
    for l in board: print(*l)

def setNum(depth):
    if depth == len(zeros):
        printBoard()
        exit()

    y,x = zeros[depth]

    for v in range(1,10):
        if not isDuplicate(y,x,v):
            board[y][x] = v
            setNum(depth + 1)
            board[y][x] = 0


board = [list(map(int, input().split())) for _ in range(MAX_SIZE)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
setNum(0)


