# 첫 번째 방을 제외하고 나머지 방은 모두 잠겨있다(시작 정점: 0)
# BFS 또는 DFS를 통해 방문한 노드의 개수를 확인하면 된다.

from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])

        def dfs(roomdId):
            if len(visited) == len(rooms):
                return

            for key in rooms[roomdId]:
                if key not in visited:
                    visited.add(key)
                    dfs(key)

        dfs(0)

        return len(visited) == len(rooms)



testCase = [
    ([[1],[2],[3],[]], True),
    ([[1,3],[3,0,1],[2],[0]],False),
    ([[2,3],[],[2],[1,3]], True),
    ([[1],[],[0,3],[1]], False)
]

for t,ans in testCase:
    print(Solution().canVisitAllRooms(t) == ans)