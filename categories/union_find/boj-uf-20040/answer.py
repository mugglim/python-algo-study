import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
ans = 0

def find(x):
    if parent[x] == x: return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    rootX = find(x)
    rootY = find(y)

    if rootX == rootY: return True

    if rootX < rootY: parent[rootY] = rootX
    else: parent[rootX] = rootY

for i in range(m):
    x,y = map(int,input().split())
    if union(x,y):
        ans = i + 1
        break

print(ans)