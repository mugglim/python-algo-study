n = int(input())
w = list(map(int,input().split()))
ans = -1


def getMaxScore(arr,cnt):

    if len(arr) < 3:
        global ans
        ans = max(ans,cnt)
        return

    for i in range(1,len(arr)-1):
        getMaxScore(arr[:i] + arr[i+1:], cnt + arr[i-1] * arr[i+1])
        

getMaxScore(w,0)
print(ans)