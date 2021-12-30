"""
주의사항 : 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
x / ababcdcd / ababcdcd 로 자르는 것은 불가능
"""

def solution(s):
    answer = len(s) # 압축되지 않는 문자열의 길이

    for length in range(1,len(s)//2 +1):
        i = 0
        temp = ""
        while i < len(s):
            pattern = s[i:i+length]
            cnt = 1
            curr = i
            # string 압축이 가능한 경우
            while pattern == s[curr+length:curr+length*2] and curr < len(s):
                cnt += 1
                curr += length

            # temp += str(cnt) + pattern
            if cnt == 1:
                temp += pattern
            else:
                temp += str(cnt) + pattern

            i = curr + length

        if len(temp) != 0: # 문자열이 압축된 경우.

            answer = min(answer,len(temp))

    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))