from itertools import permutations

def solution(n, weak, dist):
    r1,r2 = False, False
    dist.sort(reverse=True)
    # left 혹은 right로 처리한다.
    def move_left(weak,weak_combi, dist_combi):
        # boundary condition
        global r1
        if len(weak) == 0:
            r1 = True
            return True
        if len(weak_combi) == 0 and len(weak) != 0:
            r1 = False
            return False

        # 반시계방향
        left_sets = set([weak_combi[0] + i for i in range(dist_combi[0]+1)])
        move_left(weak-left_sets,weak_combi[1:],dist_combi[1:])

        return r1

    def move_right(weak, weak_combi, dist_combi):
        # boundary condition
        global r2
        if len(weak) == 0:
            r2 = True
            return True
        if len(weak_combi) == 0 and len(weak) != 0:
            r2 = False
            return False

        # 시계방향
        right_sets = set([weak_combi[0] - i if weak_combi[0] - i >= 0 else n - abs(weak_combi[0] - i) for i in
                          range(dist_combi[0] + 1)])
        move_right(weak - right_sets, weak_combi[1:], dist_combi[1:])
        return r2
    # 1. dist의 개수 만큼 순열을 돌린다.
    for i in range(1,len(dist)+1):
        for dist_combi in list(permutations(dist,i)):
            # 시계, 반시계 반향으로 어차피 동일하게 크기 표준화?
            dist_combi = [c if c < n else n for c in dist_combi]
            # 2. weak의 포인트를 시작점으로 처리한다.
            for weak_combi in list(permutations(weak,i)):
                # 3. 시계 혹은 반시계로 시작점을 기준으로 dist를 처리하여 weak를 제거한다.
                r1 = move_left(set(weak),weak_combi,dist_combi)
                r2 =  move_right(set(weak),weak_combi,dist_combi)
                if r1 == True or r2 == True:
                    return i
    return -1

# wrong.. why?
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# print(solution(200,weak = [0, 10, 50, 80, 120, 160],dist = [1, 10, 5, 40, 30]))
# print(solution(30,weak = [0, 3, 11, 21],dist = [10, 4]))
# print(solution(12,weak = [10, 0],dist = [1, 2]))