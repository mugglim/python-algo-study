from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr not in dic: dic[sortedStr] = []
            dic[sortedStr].append(str)

        return list(dic.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))

