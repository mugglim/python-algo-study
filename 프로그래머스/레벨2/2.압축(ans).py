def solution(msg):
    answer = []
    dic = {chr(64 + i):i for i in range(1, 27)}
    last = 27

    l = 0
    while l < len(msg):
        ch = msg[l] # 현재 입력
        prev = ch # 현재 입력 복원
        right = l
        isIter = False
        # 현재 입력 늘리기
        while right < len(msg) -1  and ch in dic:
            prev = ch
            right += 1
            ch += msg[right]
            isIter = True

        if isIter == False:
            l += 1
        else:
            l = right

        if l == len(msg) -1:
            if ch in dic:
                answer.append(dic[ch])
                break
            else:
                answer.append(dic[prev])
                dic[ch] = last
                last += 1
        else:
            answer.append(dic[prev])
            dic[ch] = last
            last += 1



    return answer