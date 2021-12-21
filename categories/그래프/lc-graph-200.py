# visited를 따로 선언하지 않았기에, 배열 데이터의 값 변경 위험이 있음
# 문제 풀기를 위한 구현이라고 생각.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        cnt = 0
        n, m = len(grid), len(grid[0])

        def bfs(y, x):
            queue = deque([(y, x)])
            grid[y][x] = "-1"
            while queue:
                y, x = queue.popleft()

                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == "1":
                        grid[ny][nx] = "-1"
                        queue.append((ny, nx))

        for y in range(n):
            for x in range(m):
                if grid[y][x] == '1':
                    bfs(y, x)
                    cnt += 1

        return cnt
