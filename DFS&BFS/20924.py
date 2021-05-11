# https://www.acmicpc.net/problem/20924
import sys
sys.setrecursionlimit(1000001)
input = lambda : sys.stdin.readline().rstrip()

n, root = map(int,input().split())
tree = [[] for _ in range(n+1)]
ans = [0,0]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])


def dfs(u, p, sum, f):
    if f == 0 : ans[0] = sum
    else : ans[1] = max(ans[1], sum)
    if f == 0 and len(adj[u]) > 2 - int(u == r) :
        f , sum = 1, 0
    for v,w in adj[u] :
        if v == p : continue
        dfs(v,u,sum+w,f)

dfs(r,r,0,0)
