def solution(price, money, count):
    _sum = sum([price * i for i in range(1,count+1)])
    return 0 if money >= _sum else _sum - money