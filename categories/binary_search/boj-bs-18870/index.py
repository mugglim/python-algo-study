from bisect import bisect_left

n = int(input())

arr = list(map(int,input().split()))
s = sorted(list(set(arr)))

ans = [bisect_left(s,target) for target in arr]

print(*ans)