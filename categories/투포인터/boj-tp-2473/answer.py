import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().split())))
ans = None

i = 0

while i < n - 2:
    j,k = i+1, n-1

    while j < k:
        tot = arr[i] + arr[j] + arr[k]

        if not ans or abs(tot) < abs(sum(ans)): ans = [arr[idx] for idx in [i,j,k]]

        if tot > 0: k -= 1
        else: j += 1
    i += 1

print(*ans)