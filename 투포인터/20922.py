# https://www.acmicpc.net/problem/20922

n,k = map(int,input().split())
curr = {}
l = r = 0
a = input().split()
ans = 0

def chk(key):
    if key in curr and curr[key] + 1 > k:
        return False
    return True


def remove(k):
    curr[k] -= 1
    if curr[k] == 0:
        del curr[k]

def add(k):
    if k not in curr:
        curr[k] = 1
    else:
        curr[k] += 1

while l < n:
    if r < n and chk(a[r]) == True:
        add(a[r])
        ans = max(ans,r-l+1)
        r += 1
    else:
        remove(a[l])
        l += 1


print(ans)