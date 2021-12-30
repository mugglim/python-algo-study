import sys, heapq

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)


def solution(n, s, a, b, fares):
    graph = [[] * (n + 1) for i in range(n + 1)]
    for fare in fares:
        x, y, c = fare
        graph[x].append((y, c))
        graph[y].append((x, c))

    # 다익스트라 알고리즘
    def dijkstra(start):
        distance = [INF] * (n + 1)

        heap = []
        heapq.heappush(heap, (0, start))
        distance[start] = 0

        while heap:
            dist, now = heapq.heappop(heap)
            if distance[now] < dist:
                continue

            for next in graph[now]:
                cost = dist + next[1]

                if cost < distance[next[0]]:
                    distance[next[0]] = cost
                    heapq.heappush(heap, (cost, next[0]))

        return distance

    distances = [[]]
    for i in range(1, n + 1):
        # 각 지점에서 dijkstra
        distances.append(dijkstra(i))

    answer = int(INF)
    for k in range(1, n + 1):
        if k != s:
            answer = min(
                distances[s][k] + distances[k][a] + distances[k][b],  # 경유하는 경우
                distances[s][a] + distances[s][b],  # 경유 하지 않는 경유
                answer
            )

    return answer


# 테스트
# print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))