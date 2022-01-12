def getPosNums(n):
    result = []

    while n != 0:
        result.append(n % 10)
        n = n // 10

    return result

def squareNums(nums):
    return sum([x ** 2 for x in nums])

class Solution:
    def isHappy(self, n: int) -> bool:
        squareNum = squareNums(getPosNums(n))
        if n == 1 or squareNum == 1: return True

        visited = {squareNum}
        n = squareNums(getPosNums(squareNum))

        while n not in visited:
            if n == 1: return True
            visited.add(n)
            n = squareNums(getPosNums(n))

        return False

