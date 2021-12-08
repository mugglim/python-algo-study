class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        n = len(digits)

        if n == 0: return []

        dic = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        words = [dic[x] for x in digits]

        def dfs(idx, curr):
            if idx == n:
                ans.append(curr)
                return

            for ch in words[idx]:
                dfs(idx + 1, curr + ch)

        dfs(0, "")
        return ans