import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n = int(input())
    a = {x: True for x in map(int, input().split())}
    m = int(input())
    b = map(int, input().split())

    for y in b:
        print(1 if y in a else 0)