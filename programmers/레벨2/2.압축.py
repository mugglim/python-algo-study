def solution(msg):
    answer = []
    now = 27
    dic = {chr(64 + i): i for i in range(1, now)}
    l = 0
    while l < len(msg):
        r = l
        while r < len(msg) and msg[l:r+1] in dic:
            r += 1

        if r == len(msg):
            answer.append(dic[msg[l:r]])
            break
        else:
            dic[msg[l:r+1]] = now
            answer.append(dic[msg[l:r]])
            l = r
        now += 1

    return answer
