# 1. map(f, iter)

# ex)
result = map(lambda x:x-1, map(int,input().split()))
objList = [
    {'name': "박지성", 'team': "맨유"},
    {'name': "손흥민", 'team': "토트넘"},
    {'name': "황희찬", 'team': "울버햄튼"},
]
def formatter(obj): return f"이름:{obj['name']}, 팀:{obj['team']}"
print(list(map(formatter, objList)))

# 2. reduce(f, iter, [, initValue])
from functools import reduce

nums = [1,2,3,4,5,6,10]
list2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# sum
print(reduce(lambda acc,v: acc+v, nums)) # 31

# 2d list-> 1d list
print(reduce(lambda acc, v: [*acc, *v], list2D))