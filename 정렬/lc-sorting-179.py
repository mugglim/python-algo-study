from typing import List

def mergeSort(arr):
    # 1) split
    if len(arr) == 1: return arr

    mid = len(arr) // 2

    leftArr, rightArr = arr[:mid], arr[mid:]
    sortedLeftArr, sortedRightArr = mergeSort(leftArr), mergeSort(rightArr)

    # 2) merge
    sortedArr = []
    l,r = 0,0

    while l < len(sortedLeftArr) or r < len(rightArr):
        if l == len(sortedLeftArr):
            sortedArr.extend(sortedRightArr[r:])
            break
        if r == len(sortedRightArr):
            sortedArr.extend(sortedLeftArr[l:])
            break

        if sortedLeftArr[l] + sortedRightArr[r] > sortedRightArr[r] + sortedLeftArr[l]:
            sortedArr.append(sortedLeftArr[l])
            l += 1
        else:
            sortedArr.append(sortedRightArr[r])
            r += 1

    return sortedArr


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = mergeSort(list(map(str, nums)))
        return str(int(''.join(arr)))

