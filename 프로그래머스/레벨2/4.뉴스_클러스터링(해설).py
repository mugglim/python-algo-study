from collections import Counter

def get_jiphap(str):
    a = []
    l = 0
    while l < len(str) -1:
        if str[l].isalpha() and str[l+1].isalpha():
            s = f"{str[l]}{str[l+1]}".lower()
            a.append(s.lower())
        l+=1
    return a

def solution(str1, str2):
    answer = 1
    # 만약에 교집합은 0인데, 합집합은 0이 아닌 경우
    a,b = get_jiphap(str1),get_jiphap(str2)

    # 공집합이 아닌 경우
    count_a = Counter(a)
    count_b = Counter(b)

    intersection = set(a) | set(b)

    a1 = set(a) - intersection
    b1 = set(b) - intersection

    inter_ab = sum([min(count_a[k],count_b[k]) for k in intersection])
    union_ab = sum([max(count_a[k],count_b[k]) for k in intersection]) + sum([count_a[k] for k in a1]) + sum([count_b[k] for k in b1])


    if inter_ab == 0 and union_ab == 0:
        answer = 1
    elif inter_ab !=0 and union_ab != 0:
        answer = inter_ab / union_ab
    elif inter_ab == 0 and union_ab != 0:
        answer = 0

    return int(answer*65536)



print(solution("FRANCE","french"))
print(solution("handshake","shake hands"))
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))
print(solution('a','b'))