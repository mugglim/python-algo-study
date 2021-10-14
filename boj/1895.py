from functools import reduce

r,c = map(int,input().split())
pixel = [list(map(int,input().split())) for _ in range(r)]
t = int(input())
cnt = 0

def getFilterMedian(y,x):
    filter = sorted(reduce(lambda x,y :x+y, [pixel[ny][x:x+3] for ny in range(y,y+3)]))
    return filter[4]



for i in range(r-2):
    for j in range(c-2):
        filterMedian = getFilterMedian(i,j)
        if filterMedian >= t: cnt += 1

print(cnt)