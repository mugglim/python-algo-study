n = int(input())
a = sorted(list(map(int,input().split())))


lo = 0
hi = n-1
ans = [[a[lo], a[hi]], abs(a[lo] + a[hi])]

while lo < hi:
    diff = a[lo] + a[hi]

    if abs(diff) < ans[1]:
        ans = [[a[lo], a[hi]], abs(diff)]
        if diff == 0: break

    if diff < 0: lo += 1
    else: hi -= 1

print(*ans[0])
