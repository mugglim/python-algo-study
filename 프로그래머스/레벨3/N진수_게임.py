from collections import deque

dic = {i:str(i) for i in range(10)}
dic.update({i:chr(55+i) for i in range(10,16)})

def get_base(n,div):
    tmp = deque()
    if n == 0:
        return "0"
    while n > 0:
        tmp.appendleft(dic[n%div])
        n = n // div

    return "".join(tmp)


def solution(n, t, m, p):
    result = ""
    i = 0
    order = 1
    now = 0
    tmp = deque(list(get_base(now, n)))
    while i != t:
        is_find = False
        while tmp:
            pop = tmp.popleft()
            if order == p:
                result += pop
                is_find = True
                i += 1
                break
            order = order + 1 if order < m else 1

        if is_find == True:
            order = order + 1 if order < m else 1

        if not tmp:
            now += 1
            tmp = deque(list(get_base(now,n)))

    return result


