answer = 0

n, m = map(int, input().split())
a = list(map(int, input().split()))


# 눈덩이의 시작 크기는 1 이다. 눈덩이의 시작 위치는 0 이다.
def dfs(idx, val, cnt):
    if cnt == m or idx == n - 1:
        global answer
        answer = max(answer, val)
        return

    if idx + 1 < n:
        dfs(idx + 1, val + a[idx + 1], cnt + 1)
    if idx + 2 < n:
        dfs(idx + 2, val // 2 + a[idx + 2], cnt + 1)


# idx, val, cnt
dfs(-1, 1, 0)
print(answer)