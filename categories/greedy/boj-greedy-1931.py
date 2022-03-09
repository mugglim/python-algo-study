import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

meeting_time_list = [list(map(int,input().split())) for _ in range(n)]
meeting_time_list.sort(key=lambda x:(x[1],x[0]))
curr = 0
cnt = 0

for s,e in meeting_time_list:
    if curr <= s:
        cnt += 1
        curr = e

print(cnt)