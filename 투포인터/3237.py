n = int(input())
a = sorted(list(map(int,input().split())))
x = int(input())

ans = 0
l,r = 0, n -1

while(l < r):
    total = a[l] + a[r]
    if total == x:
        ans += 1
        l += 1
    elif total < x:
        l += 1
    elif total > x:
        r -= 1

print(ans)