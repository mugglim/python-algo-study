class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # O(N)
        dic = {x: True for x in jewels}

        # O(N) + O(N) = O(N)
        return sum([1 if ch in dic else 0 for ch in stones])