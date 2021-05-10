# https://www.acmicpc.net/problem/20920

import sys
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
words = {}

for _ in range(n):
    word = input()
    if len(word) >= m:
        if word not in words:
            words[word] = 1
        words[word] += 1


words = [l[0] for l in sorted(list(words.items()),key=lambda x:(-x[-1],-len(x[0]),x))]

for x in words:
    print(x)