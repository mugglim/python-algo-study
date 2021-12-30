import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
milks = [0] * (n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())
queries = [list(map(int,input().split())) for _ in range(q)]

def dfs(curr, target, depth, trace):
    if curr == target: return True

    for adj in graph[curr]:
        if adj not in trace:
            trace.add(adj)

            if dfs(adj, target, depth + 1, trace):
                milks[adj] += depth + 1
                return True
            trace.remove(adj)

    return False


for query in queries:
    cmd = query[0]

    if cmd == 1:
        start, target = query[1:]
        dfs(start, target, 0, {start})
    else:
        print(milks[query[1]])


