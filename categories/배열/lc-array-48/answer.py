from typing import List

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for y in range(n//2 + 1):
            for x in range(y, n-y-1):
                prev = matrix[y][x]
                curr = [y,x, prev]
                for _ in range(4):
                    # 1) 다음 좌표를 계산한다.
                    dy,dx = curr[1] - curr[0], n -1 - (curr[0] + curr[1])
                    ny,nx = curr[0] + dy, curr[1] + dx

                    # 2) 다음 좌표에 있는 값을 저장한다.
                    prev = matrix[ny][nx]

                    # 3) swap 한다.
                    matrix[ny][nx] = curr[-1]

                    # 4) 다음 좌표를 반영한다.
                    curr = [ny,nx, prev]



Solution().rotate(matrix)
