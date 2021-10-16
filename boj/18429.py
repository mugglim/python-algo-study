ans = 0
n,k = map(int,input().split())
a = list(map(int,input().split()))
visited = [False for _ in range(n)]

def backtrack(curr, cnt):
    # 종료 조건
    if cnt == n:
        global ans
        ans += 1
        return

    # 재귀 조건
    for i in range(n):
        v = a[i]
        if v + curr >= k and visited[i] == False:
            visited[i] = True
            backtrack(v + curr - k, cnt + 1)
            visited[i] = False


for i in range(n):
    if a[i] >= k:
        visited[i] = True
        backtrack(a[i]-k, 1)
        visited[i] = False


print(ans)

