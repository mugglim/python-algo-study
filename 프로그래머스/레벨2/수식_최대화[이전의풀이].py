import re
from itertools import permutations


def solution(expression):
    answer = 0
    # 연산자 기준으로 split 하기
    nums = list(map(int, re.split("[+|*|-]", expression)))
    # 연산자만 찾기
    opers = re.findall("[+|*|-]", expression)

    for oper in list(permutations(set(opers), len(set(opers)))):
        tmp_nums, tmp_opers = nums[::], opers[::]
        for op in oper:
            i = 0
            while i < len(tmp_opers):
                if tmp_opers[i] == op:  # 해당 문자에 해당하는 경우
                    if op == "*":
                        tmp_nums.insert(i, tmp_nums[i] * tmp_nums[i + 1])
                    elif op == "+":
                        tmp_nums.insert(i, tmp_nums[i] + tmp_nums[i + 1])
                    elif op == "-":
                        tmp_nums.insert(i, tmp_nums[i] - tmp_nums[i + 1])
                    del tmp_nums[i + 1]
                    del tmp_nums[i + 1]
                    del tmp_opers[i]
                else:
                    i += 1

        answer = max(answer, abs(tmp_nums[0]))

    return answer


# print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))