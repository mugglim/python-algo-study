import sys
input = lambda: sys.stdin.readline().rstrip()

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
t = int(input())

for _ in range(t):
    n = int(input())
    if n >= len(dp):
        for i in range(len(dp), n+1):
            dp.append(dp[i-2] + dp[i-3])
    print(dp[n])

    print(dp)