class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # x ^ y ^ y = x ^ (y^y)  = x ^ 0 = x

        # a^b^c^d = (a^b)^(c^d)
        # (a^b^c^d)^(c^d) = (a^b)^(c^d)^(c^d)
        # (a^b^c^d)^(c^d) = (a^b)

        result = []
        prefix = [0]
        total = 0

        for n in arr:
            total ^= n
            prefix.append(total)

        for l, r in queries:
            result.append(prefix[r + 1] ^ prefix[l])

        return result