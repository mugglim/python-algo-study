import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
mi = lambda: map(int,input().split())

n,r,q = mi()
graph = [[] for _ in range(n+1)]
dp = [0] * (n+1)
visitied = [False] * (n+1)
ans = []

def dfs(root):
    cnt = 1

    visitied[root] = True

    for child in graph[root]:
        if not visitied[child]:
            cnt += dfs(child)

    visitied[root] = False

    dp[root] = cnt
    return dp[root]

for _ in range(n-1):
    a,b, = mi()
    graph[a].append(b)
    graph[b].append(a)


dfs(r)

for _ in range(q):
    a = int(input())
    ans.append(str(dp[a]))


print('\n'.join(ans))
