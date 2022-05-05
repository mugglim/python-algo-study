import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
prefix = [0] * (n+1)
board = list(map(int,input().split()))


for _ in range(m):
    a,b,k = map(int,input().split())
    a,b = a-1, b-1

    prefix[a] += k
    prefix[b+1] -= k

for i in range(1, n+1):
    prefix[i] += prefix[i-1]

for i in range(n):
    prefix[i] += board[i]

print(*prefix[:-1])