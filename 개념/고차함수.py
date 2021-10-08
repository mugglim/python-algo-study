from functools import reduce

# map의 return 값은 객체이다.
# reduce는 초기값을 설정할 수 있다.

nums = [1,2,3,4,5,6,10]
arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
objList = [
    {'name': "박지성", 'team': "맨유"},
    {'name': "손흥민", 'team': "토트넘"},
    {'name': "황희찬", 'team': "울버햄튼"},
]

# sum
print(reduce(lambda x,y: x+y, nums)) # 31
print(reduce(lambda x,y: x+y, nums,10)) # 41
print(reduce(lambda x,y: x+y, nums,100)) # 131


# 2d -> 1d
print(reduce(lambda prev, next: [*prev, *next], arr1))

# obj -> string
print(list(map(lambda obj: f"이름:{obj['name']}, 팀:{obj['team']}",objList)))