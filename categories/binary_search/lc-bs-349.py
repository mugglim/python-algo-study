import bisect

def binarySearch(arr, target):
    idx = bisect.bisect_left(arr, target)
    return 0 <= idx < len(arr) and arr[idx] == target


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # (1) binary_search
        dic = {}

        nums1.sort()
        nums2.sort()

        for n in nums1:
            isExist = binarySearch(nums2, n)
            if n not in dic and isExist: dic[n] = True

        return dic.keys()

        # (2) set 자료구조 이용
        # nums1,nums2 = set(nums1), set(nums2)
        # return list(nums1.intersection(nums2))