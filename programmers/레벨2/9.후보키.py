from itertools import combinations

def solution(relation):
    answer = 0
    col = [i for i in range(len(relation[0]))]
    tuple_length = len(relation)

    key_list = {}

    # 유일성 검사
    for i in range(1,len(col)+1):
        for col_list in combinations(col,i):
            tuple = set()
            for j in range(tuple_length):
                tmp = ""
                for k in col_list:
                    tmp += relation[j][k]
                tuple.add(tmp)
            if tuple_length == len(tuple):
                key_list[''.join(list(map(str,col_list)))] = True

    # print(key_list)

    def check_minimality(key):
        for i in range(len(key)):
            for a in combinations(list(key),i):
                if "".join(a) in key_list:
                    return False
        return True
    # 최소성 검사
    for k in key_list.keys():
        answer += 1 if check_minimality(k) == True else 0

    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])