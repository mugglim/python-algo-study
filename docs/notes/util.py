import math


# get length of digit
def getDigitLength(n):
    return int(math.log10(n)) + 1


# sorting number by place value => Ex) 9 > 89, 99 > 100
def sortByPlaceValue(arr):
    # use merge sort for sorting
    # time : O(nlogn)

    # 1) split
    if len(arr) == 1: return arr

    mid = len(arr) // 2

    leftArr, rightArr = arr[:mid], arr[mid:]
    sortedLeftArr, sortedRightArr = sortByPlaceValue(leftArr), sortByPlaceValue(rightArr)

    # 2) merge
    sortedArr = []
    l, r = 0, 0

    while l < len(sortedLeftArr) or r < len(rightArr):
        if l == len(sortedLeftArr):
            sortedArr.extend(sortedRightArr[r:])
            break
        if r == len(sortedRightArr):
            sortedArr.extend(sortedLeftArr[l:])
            break

        # π Tip: λ μ«μλ₯Ό λ ν΄μ μλ¦Ώμλ₯Ό λ§μΆ ν λΉκ΅νλ©΄ λλ€!
        # λ¨, λ¬ΈμνμΌλ‘ λ°°μ΄μ νλ³ν ν΄μ£Όμ΄μΌλ§ μλμ λ‘μ§μ΄ λμνλ€.
        # Ex) 12, 9 => 129, 912
        # ref : https://github.com/onlybooks/algorithm-interview/blob/master/5-algorithms/ch17/61-1.py
        if sortedLeftArr[l] + sortedRightArr[r] <= sortedRightArr[r] + sortedLeftArr[l]:
            sortedArr.append(sortedLeftArr[l])
            l += 1
        else:
            sortedArr.append(sortedRightArr[r])
            r += 1

    return sortedArr
