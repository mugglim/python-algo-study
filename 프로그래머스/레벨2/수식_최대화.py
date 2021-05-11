import re
from itertools import permutations
def solution(expression):
    answer = 0

    nums = re.split("[+|*|-]",expression)
    oper_idx = re.findall("[+|*|-]",expression)
    expression = []
    for a,b in zip(nums[:-1],oper_idx):
        expression.append(a)
        expression.append(b)
    expression.append(nums[-1])

    for opt in list(permutations(["*","+","-"],3)):
        answer = max(cal_by_order(expression,opt),answer)

    return answer

def cal_by_order(nums,order_opt):
    if len(nums) == 1:
        return abs(nums[0])

    while order_opt[0] in nums:
        idx = nums.index(order_opt[0])
        new_val = eval(f"{nums[idx-1]}{order_opt[0]}{nums[idx+1]}")
        nums = nums[:idx-1] + [new_val] + nums[idx+2:]

    return cal_by_order(nums,order_opt[1:])


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))