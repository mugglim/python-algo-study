n = int(input())
m = int(input())
a = sorted(list(map(int,input().split())))

cnt = 0
l,r = 0, len(a) -1


while l < r:
    total = a[l] + a[r]

    if total <= m:
        if total == m : cnt += 1
        l += 1
    else: r -= 1

print(cnt)