import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input())
s = input()
ans = []
l = r = 0

queue = []

def cal(a,opt,b):

    if opt == "U":
        if a < 0 or b < 0:
            return -(abs(a)//abs(b))
        return a // b
    if opt == "S":
        return a-b
    if opt == "M":
        return a*b
    if opt == "P":
        return a+b

while l < len(s):
    if s[l].isdigit():
        r = l
        while s[r].isdigit() and r < len(s):
            r += 1
        num = int(s[l:r])
        if not queue:
            queue.append(num)
        else:
            queue = [cal(queue[0],queue[1],num)]
        l = r
    else:
        if s[l] == "C":
            ans.append(queue[0])
        else:
            queue.append(s[l])
        l += 1

if ans:
    print(*ans)
else:
    print("NO OUTPUT")