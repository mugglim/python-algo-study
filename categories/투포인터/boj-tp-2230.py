import sys
input = sys.stdin.readline

INF = int(1e10)

n,m = map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])
ans = INF

r = 0

for l in range(n):
    while r < n and arr[r] - arr[l] < m: r += 1
    if r == n: break
    ans = min(ans, arr[r] - arr[l])

print(ans)