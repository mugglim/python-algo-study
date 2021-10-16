import sys
input = lambda: sys.stdin.readline().rstrip()

r,c,q = map(int,input().split())
pixel = [list(map(int,input().split())) for _ in range(r)]
_sum = 0
ans = []

pixel_prefix = [[0] for _ in range(r)]

for i in range(r):
    _sum = 0
    for j in range(c):
        _sum += pixel[i][j]
        pixel_prefix[i].append(_sum)


for _ in range(q):
    r1,c1,r2,c2  = map(lambda x:x-1,map(int,input().split()))
    _sum = 0

    for i in range(r1,r2+1):
        _sum += pixel_prefix[i][c2+1] - pixel_prefix[i][c1]

    _avg = _sum // ((r2-r1+1)*(c2-c1+1))
    print(_avg)