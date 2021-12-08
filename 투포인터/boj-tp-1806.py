import sys
input = sys.stdin.readline

INT = int(1e5 + 1)

n,s = map(int,input().split())
arr = list(map(int,input().split()))
ans = INT

r = 0
total = arr[0]

for l in range(n):
    while r < n and total < s:
        r += 1
        if r != n: total += arr[r]

    if r == n: break
    if total >= s: ans = min(ans, r - l + 1)
    total -= arr[l]


print(ans if ans != INT else 0)