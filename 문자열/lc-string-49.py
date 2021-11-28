class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 애너그램은 문자(char) 개수 및 종류가 똑같은 것
        # O(NlogN) : 정렬(팀 소트)
        # O(N) : 배열 순회
        # 계산 : O(N^2logN)
        # 출력 : O(N)

        dic = {}

        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in dic: dic[sortedS] = []
            dic[sortedS].append(s)

        return dic.values()