def rotate(l):
    result = []
    for j in range(len(l)):
        tmp = []
        for i in range(len(l)-1,-1,-1):
            tmp.append(l[i][j])
        result.append(tmp)
    return result

def check(key,lock):
    n,m = len(key),len(lock)
    lock_points = 0 # 좌물쇠 홈의 개수
    for i in range(m):
        for j in range(m):
            if lock[i][j] == 0:
                lock_points += 1

    if lock_points == 0:
        return False

    # 좌측 상단
    for size in range(1,min(n,m)+1):
        cnt = 0

    return False

def solution(key, lock):

    key1 = rotate(key) # 90 도
    key2 = rotate(key1) # 180도 
    key3 = rotate(key2) # 270도

    return check(key,lock) or check(key1,lock) or check(key2,lock) or check(key3,lock)


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))