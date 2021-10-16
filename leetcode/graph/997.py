class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [[0, False] for _ in range(n)]
        answer = - 1

        for l in trust:
            a, b = l[0] - 1, l[1] - 1
            graph[a][1] = True
            graph[b][0] += 1

        for i in range(n):
            p = graph[i]
            print(p[0], p[1], p[0] == n - 1, p[1] == False)

            if p[0] == n - 1 and p[1] == False:
                answer = i + 1
                break

        return answer