import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())

degree_name = []
degree_score = []

def get_degree(score):
    lbd_idx = bisect_left(degree_score, score)
    max_lbd_idx = max(lbd_idx + 1, n - 1)

    return degree_name[lbd_idx] if score <= degree_score[lbd_idx] else degree_name[max_lbd_idx]

for _ in range(n):
    a,b = input().split()
    degree_name.append(a)
    degree_score.append(int(b))

for _ in range(m):
    score = int(input())
    print(get_degree(score))
