import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # 굳이 sqrt 할 필요 없음
        def getDist(x,y):
            return (x ** 2 + y ** 2) ** 0.5

        heap = []
        result = []

        for x,y in points:
            heapq.heappush(heap, (getDist(x,y),x,y))

        for _ in range(k):
            result.append(list(heapq.heappop(heap)[1:]))

        return result