n,k = map(int,input().split())
minSum = (k*(k+1))//2
ans = -1
startNum = 1
idx = 0
arr = [0 for _ in range(k)]


def sumRange(p,q):
    return int(((q-p+1)/2)*(p+q))


# 1. 연속된 수가 담기는 경우 => Ex) 7,3 => (1,2,4)
# 2. 연속되지 않는 수가 담기는 경우 => Ex) 6,3 = (1,2,3)
if minSum <= n:
    while idx < k:
        while True:
            _sum = sumRange(startNum, k+startNum-idx-1)
            if _sum > n - sum(arr):
                arr[idx] = startNum - 1
                break
            startNum += 1
        idx += 1
    ans = arr[-1] - arr[0]

print(ans)