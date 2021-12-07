"""
nums : 정수 배열

정의
    - 3개의 element를 선택하여 합이 0인 경우의 element 들을 반환
    - 결과에 중복 된 값이 있으면 안 됨. Ex) [[-1,-1,2], [-1,-1,2]] 
해결
    1) 배열을 순회하면서 element 고정
    2) 해당 값 이전 index, 이후 index의 배열을 생성
    3) 이후 two-sum과 유사하게 hash-table로 관리
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def getTargetArray(arr, target):  # O(N)
            l, r = 0, len(arr) - 1
            result = []

            while l < r:
                total = arr[l] + arr[r]

                if total == target:
                    result.append([arr[l], arr[r]])
                    l += 1
                if total < target: l += 1
                if total > target: r -= 1

            return result

        nums.sort()
        visited = {}
        result = {}

        for i in range(len(nums) - 2):  # O(N)
            target = -nums[i]
            subArr = nums[i + 1:]

            # target이 중복되면 굳이 탐색할 필요가 없음
            if target not in visited:
                visited[target] = True
                for l in getTargetArray(subArr, target):
                    key = tuple([-target, *l])
                    if key not in result: result[key] = True

        return [[*k] for k in result.keys()]
# for testing
tc = [
    [-1,0,1,2,-1,-4],
    # [-1,0,1,2,-1,-4,-2,-3,3,0,4],
    # [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
]

for l in tc:
    print(Solution().threeSum(l))
