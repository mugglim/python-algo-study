class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0

        while num > 0:
            # 마지막 bit가 0이라면, 그냥 1을 빼주면 됨.
            num = num -1 if num & 1 else num >> 1
            cnt += 1
        return cnt