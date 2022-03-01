import sys
input = lambda: sys.stdin.readline().rstrip()

dp = {}
ans = []

def w(a,b,c):
    if (a,b,c) in dp: return dp[(a,b,c)]

    if a <= 0 or b <= 0 or c <= 0: return 1
    elif a > 20 or b > 20 or c > 20:
        if (20,20,20) not in dp:
            dp[(20,20,20)] = w(20,20,20)
        dp[(a,b,c)] = dp[(20,20,20)]
    elif a < b < c:
        dp[(a,b,c)] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        dp[(a,b,c)] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[(a,b,c)]


while True:
    a,b,c = map(int,input().split())
    if a == b == c == -1: break
    ans.append(f"w{a,b,c} = {w(a,b,c)}")

for tc in ans: print(tc)
