from bisect import bisect_left

n = int(input())
arr = list(map(int,input().split()))

def get_lis_length(arr):
    dp = [arr[0]]

    for i,x in enumerate(arr[1:]):
        if dp[-1] < x: dp.append(x)
        else: dp[bisect_left(dp, x)] = x

    return len(dp)

print(get_lis_length(arr))