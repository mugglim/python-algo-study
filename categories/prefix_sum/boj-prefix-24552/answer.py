import sys
input = lambda: sys.stdin.readline().rstrip()

dic = { "(" : 1, ")" : -1 }

s = input()
prefix = [[0,0,0,0]] # 누적합, 0의개수, -2의 개수, 음수 존재 여부
tot = [0,0,0,0]
cnt = 0

for ch in s:
    tot[0] += dic[ch]

    if tot[0] == 0: tot[1] += 1
    if tot[0] == -2: tot[2] += 1
    if tot[0] < 0: tot[3] += 1
    prefix.append([*tot])


for i, ch in enumerate(s):
    v = dic[ch]
    is_tot_zero = prefix[-1][0] - v == 0
    can_remove_open_bracket = prefix[i][3] == 0 and prefix[-1][1] - prefix[i+1][1] == 0
    can_remove_close_bracket = prefix[i][3] == 0 and prefix[-1][2] - prefix[i+1][2] == 0

    if is_tot_zero and ((v == 1 and can_remove_open_bracket) or (v == -1 and can_remove_close_bracket)):
        cnt += 1

print(cnt)
