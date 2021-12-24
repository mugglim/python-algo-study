import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())

files = [input().split(".") for _ in range(n)]
extensions = set(input() for _ in range(m))

ans = sorted(files, key=lambda x:(x[0], not x[1] in extensions, x[1]))
for l in ans: print('.'.join(l))

