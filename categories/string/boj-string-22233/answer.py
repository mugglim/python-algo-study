import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
keywords = set(input() for _ in range(n))
ans = []

for _ in range(m):
    words = input().split(",")
    for word in words:
        if word in keywords: keywords.remove(word)

    ans.append(len(keywords))


for x in ans: print(x)