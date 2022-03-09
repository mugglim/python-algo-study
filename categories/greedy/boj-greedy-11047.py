import sys
input = lambda: sys.stdin.readline().rstrip()

n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
idx = 1
remain = k
cnt = 0

while idx <= len(coins) and remain > 0:
    coin = coins[-idx]

    if remain // coin > 0:
        cnt += remain // coin
        remain %= coin

    idx += 1
print(cnt)
