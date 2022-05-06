import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = sorted([int(input()) for _ in range(n)])

# {(x_i+y_i)}
two_sum_list = sorted([a[i]+a[j] for i in range(n) for j in range(n)])
ans = -1

for i in range(n):
    for j in range(n):
        # x+y+z = k => x+y = k-z
        z,k = a[i], a[j]
        lbd_idx = bisect_left(two_sum_list, k-z)
        if two_sum_list[lbd_idx] == k-z: ans = max(ans, k)

print(ans)
