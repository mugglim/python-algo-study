import sys
input = lambda:sys.stdin.readline().rstrip()
n,m,h = map(int,input().split())
ans = 0
board = []
start = [0,0]
milkList = []

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j] == 1: start = [i,j]
        elif row[j] == 2: milkList.append([i,j])
    board.append(row)


def dfs(curr, cnt, hp):
    global ans
    y,x = curr

    returnDist = abs(y - start[0]) + abs(x - start[1])
    if hp >= returnDist: ans = max(ans, cnt)

    for milk in milkList:
        ny, nx = milk
        dist = abs(ny-y) + abs(nx-x)
        newHp = hp + h - dist

        if board[ny][nx] == 2 and hp >= dist:
            board[ny][nx] = 0
            dfs([ny,nx],cnt+1,newHp)
            board[ny][nx] = 2

dfs(start,0,m)
print(ans)