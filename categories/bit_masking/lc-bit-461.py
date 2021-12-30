class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 0 + 0 => False
        # 0 + 1 => True
        # 1 + 1 => False
        # XOR 연산 하고, 1의 개수만 체크하면 됨.

        def countOneBit(n):
            cnt = 0
            while n > 0:
                n = n & (n - 1)
                cnt += 1
            return cnt

        result = countOneBit(x ^ y)
        return result
