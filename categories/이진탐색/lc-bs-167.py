import bisect


def binarySearch(arr, target, lo):
    idx = bisect.bisect_left(arr, target, lo)
    isExist = idx < len(arr) and arr[idx] == target
    return idx if isExist else False


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, x in enumerate(numbers):
            targetIdx = binarySearch(numbers, target - x, i + 1)
            if targetIdx: return [i + 1, targetIdx + 1]