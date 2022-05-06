import sys
input = lambda : sys.stdin.readline().rstrip()
INF = sys.maxsize

t = int(input())

for _ in range(t):
    n,p,q = map(int,input().split())
    s_list = [int(input()) for _ in range(n)]
    costs = [[INF] * (p+1) for _ in range(p+1)]
    ans = [-1, INF]

    for _ in range(q):
        a,b,c = map(int,input().split())
        costs[a][b] = min(costs[a][b],c)
        costs[b][a] = min(costs[b][a],c)

    for i in range(1, p+1): costs[i][i] = 0

    for k in range(1, p+1):
        for a in range(1, p+1):
            for b in range(1, p+1):
                costs[a][b] = min(costs[a][b], costs[a][k] + costs[k][b])

    for i in range(1, p+1):
        total_cost = sum([costs[s][i] ** 2 for s in s_list])

        if total_cost < ans[1]:
            ans = [i, total_cost]

    print(*ans)
