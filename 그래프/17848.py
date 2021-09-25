n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

ans = int(1e10)
dx = [-1,0,1]
dy = [1,1,1]


def dfs(y,x,d,cnt):

    for i in range(3):
        ny,nx = y+dy[i], x+dx[i]
        
        if ny == n and 0 <= nx < m:        
            global ans
            ans = min(ans,cnt)
            return;
    
        if 0 <= ny < n and 0 <= nx < m and (d == - 1 or d != i):
            dfs(ny,nx,i,cnt + a[ny][nx])




startPtList = [[0,i] for i in range(m)]

for l in startPtList:
    y,x = l
    cnt = a[y][x]

    dfs(y,x,-1,cnt)


print(ans)
