# 저가에 사서 고가에 팔자!

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        ans = 0

        for x in prices:
            curr = min(curr, x)
            ans = max(ans, x - curr)

        return ans

