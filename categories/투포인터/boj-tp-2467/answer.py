import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ans = None

l,r = 0, n -1

while l < r:
    diff = arr[r] + arr[l]
    if not ans or abs(diff) < abs(sum(ans)): ans = [arr[l], arr[r]]

    if diff > 0: r-=1
    else: l += 1

print(*ans)


