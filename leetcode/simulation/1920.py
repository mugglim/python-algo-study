class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return reduce(lambda a,b:[*a,nums[b]] ,nums,[])