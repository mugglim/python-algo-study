def solution(s):
    answer = len(s) # No 압축

    for i in range(1, len(s)//2 + 1):
        if i == 8:
            print("@")
        tmp = ""
        l = 0
        cnt = 1

        while l < len(s):
            r = l + i
            while r < len(s) and s[l:l+i] == s[r:r+i]:
                cnt += 1
                r += i

            if r >= len(s) and cnt <= 1:
                tmp += s[l:]
                break

            if cnt > 1:
                tmp += f"{cnt}{s[l:l+i]}"
                cnt = 1
            else:
                tmp += s[l:l+i]
            l = r

        answer = min(answer, len(tmp))

    print(answer)
    return answer

solution("aabbaccc")