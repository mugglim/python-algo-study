from itertools import combinations


def solution(relation):
    # 유일성 : 해당 값이 유일한 UNIQUE해야함.
    # 최소성 : 속성 집합 중 하나 이상을 제외더라도 유일성을 만족하는 경우
    # 그러면, 최소성은 속성이 적을수록 만족하는 것이 아닌가?
    # 즉, 최소성은 이미 유일성을 만족하는 속성 집합이 다른 속성을 부분집합으로 가지면 안된다.
    # 왜냐하면 유일성을 만족하는 부분집합을 제거하면 유일성이 깨지기 떄문이다.
    answer = []
    dic = {}
    coluums = [i for i in range(len(relation[0]))]
    rows = len(relation)

    # 속성을 고르는 개수
    for i in range(1, len(coluums) + 1):
        for attribute in list(combinations(coluums, i)):
            isAlreaySet = False

            # 최소성 검사
            l = [list(combinations(list(attribute), k)) for k in range(1, i)]
            for l1 in l:
                for x in l1:
                    if "".join(list(map(str, list(x)))) in dic:
                        isAlreaySet = True
                        break
                if isAlreaySet == True:
                    break
            if isAlreaySet == True:
                continue

            # 유일성 검사
            temp = set()
            for j in range(rows):
                temp.add("".join([relation[j][a] for a in attribute]))

            if len(temp) == rows:
                dic["".join(list(map(str, list(attribute))))] = True

    return len(dic)


print(
    solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
              ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
)