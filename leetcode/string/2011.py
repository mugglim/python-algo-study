class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return reduce(lambda a,b: a+1 if "+" in b else a-1, operations, 0)