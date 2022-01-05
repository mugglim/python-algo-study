from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uamList = [0] * k

        dic = {}

        for userId, userTime in logs:
            if userId not in dic: dic[userId] = {}
            if userTime not in dic[userId]: dic[userId][userTime] = True

        for timeList in dic.values():
            uamList[len(timeList) - 1] += 1

        return uamList
