class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        # iterate O(N)
        for n in nums:
            if n not in dic: dic[n] = 0
            dic[n] += 1

        # iterate O(N)
        # sorting by value : O(nlogn)
        data = sorted(dic.items(), key=lambda x: -x[1])

        return [*map(lambda x: x[0], data[:k])]

