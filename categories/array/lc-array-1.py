"""
# 정의
    nums : 정수 array, target: 정수
    nums에서 두 element를 더해 target이 되는 index를 array를 반환
    해답은 정확히 1개
# 해결
    1. nums를 순회한다.
        1) element를 hash table로 관리한다. (key: element, value : index)
        2) target - element가 hash table에 있다면 순회를 종료
# 결론
    Big-O : O(N)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        result = None

        for i, x in enumerate(nums):
            diff = target - x
            if diff in dic:
                result = [dic[diff], i]
                break
            else:
                dic[x] = i

        return result
