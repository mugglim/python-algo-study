from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        stack = []
        arr = sorted(candidates)

        def dfs(curr = 0, leftPivot = 0):
            if curr == target:
                result.append([*stack])
                return

            for x in arr:
                if curr + x > target: break

                if x - leftPivot >= 0:
                    stack.append(x)
                    dfs(curr + x, x)
                    stack.pop()


        dfs()
        return result



