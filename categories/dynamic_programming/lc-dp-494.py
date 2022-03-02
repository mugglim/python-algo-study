class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(idx, tot):
            if idx == len(nums): return 1 if tot == target else 0

            k = (idx, tot)
            if k in dp: return dp[k]

            dp[k] = backtrack(idx + 1, tot + nums[idx]) + backtrack(idx + 1, tot - nums[idx])
            return dp[k]

        backtrack(0, 0)
        return dp[(0, 0)]