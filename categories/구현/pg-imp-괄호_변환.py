# 올바믄 괄호 문자열 확인
def check1(s):
    stack = []
    for x in s:
        if x == "(":
            stack.append("(")
        elif x == ")":
            if not stack:
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

def split_u_v(s):
    a,b = 0,0
    i = 0
    while i < len(s):
        if s[i] == ")":
            a += 1
        elif s[i] == "(":
            b += 1

        if a == b:
            i += 1
            break
        i += 1

    return [s[:i],s[i:]]

def switch_bracket(s):
    tmp = ""
    for x in s:
        tmp += ")" if x == "(" else "("
    return tmp

def solution(p):
    # 1.
    if p == "":
        return ""
    # 2.
    u,v = split_u_v(p)

    # 3.
    if check1(u) == True:
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + switch_bracket(u[1:-1])

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))