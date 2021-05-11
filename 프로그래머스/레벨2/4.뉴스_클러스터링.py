from collections import Counter

def check(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False

def solution(str1, str2):
    answer = 0
    # 전처리
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if check(str1[i:i+2]) == True]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if check(str2[i:i+2]) == True]


    if len(str1) == 0 and len(str2) == 0:
        answer = 1
    else:
        str1 = Counter(str1)
        str2 = Counter(str2)
        hap, kyo = 0,0

        for k in str1.keys():
            if k in str2:
                hap += max(str1[k],str2[k])
                kyo += min(str1[k],str2[k])
                del str2[k]
            else:
                hap += str1[k]

        for k in str2.keys():
            hap += str2[k]

        answer = kyo / hap



    return int(65536*answer)

print(solution("FRANCE","french"))