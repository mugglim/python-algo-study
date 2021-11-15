class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[0][0] = grid[0][0]
        # dp[y][x] = dp[y][x-1] + grid[y][x] (y = 0, x >= 1)
        # dp[y][x] = dp[y-1][x] + grid[y][x] (y >= 1, x = 0)
        # dp[y][x] = min(dp[y][x-1], dp[y-1][x]) + grid[y][x] (y >= 1, x >= 1)

        n = len(grid)
        m = len(grid[0])

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]

        # row
        for x in range(1, m): dp[0][x] = dp[0][x - 1] + grid[0][x]
        for y in range(1, n): dp[y][0] = dp[y - 1][0] + grid[y][0]

        for y in range(1, n):
            for x in range(1, m):
                dp[y][x] = min(dp[y][x - 1], dp[y - 1][x]) + grid[y][x]

        return dp[n - 1][m - 1]

