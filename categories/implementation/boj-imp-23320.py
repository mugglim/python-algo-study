import math
n = int(input())
scores = list(map(int,input().split()))
x,y = map(int,input().split())

a1 = math.floor(n * x * 0.01)
a2 = len([True for score in scores if score >= y])

print(a1,a2)