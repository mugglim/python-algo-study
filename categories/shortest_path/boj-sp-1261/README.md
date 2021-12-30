## 링크
https://www.acmicpc.net/problem/1261

## 풀이 1

(1,1) -> (N,M)으로 이동할 때 벽을 최소한으로 부시는 경우를 구해야한다.  
BFS로 탐색을 하면서 방문을 했더라도 벽을 부순 횟수가 더 적다면 다시 방문하는 방법을 적용했다.

그런데, pypy3로 제출 시 통과되고 python은 시간 초과가 발생했다.

### code
```python
import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
INF = int(1e5)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int, input().split())

def isOutOfBounds(y,x): return y < 0 or y >= n or x < 0 or x >= m

board = [list(map(int,list(input()))) for _ in range(n)]
crashed = [[INF for _ in range(m)] for _ in range(n)]

ans = 0

queue = deque([(0,0,0)])
crashed[0][0] = 0

while queue:
    y,x,crash = queue.popleft()

    for k in range(4):
        ny,nx = y+dy[k], x+dx[k]

        if not isOutOfBounds(ny,nx):
            newCrash = crash + 1 if board[ny][nx] == 1 else crash

            if newCrash < crashed[ny][nx]:
                crashed[ny][nx] = newCrash
                queue.append((ny,nx,newCrash))

print(crashed[n-1][m-1])
```

## 풀이 2
python으로 제출 시 통과 여부가 궁금하여 확인한 결과 1000ms 이내의 코드를 작성해야 한다.  
풀이 1에서 최소한으로 벽을 부수면서, 최단 거리로 이동하는 경우의 수를 생각해봤다..

생각해보니.. 벽이 있는 경우와 없는 경우는 가중치가 다르기 때문에 다익스트라를 적용할 수 있을 것 같다.
(벽이 없는 경우:0, 있는 경우:1)

```python
import sys
import heapq
input = lambda:sys.stdin.readline().rstrip()
INF = int(1e5)

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def isOutOfBounds(y,x): return y < 0 or y >= n or x < 0 or x >= m

def dijkstra(graph,start,end):
    n,m = len(graph), len(graph[0])
    costs = [[INF] * m for _ in range(n)]

    s_y, s_x = start
    e_y, e_x = end

    heap = [(0, s_y, s_x)]
    costs[s_y][s_x] = 0

    while heap:
        cost, y,x = heapq.heappop(heap)

        if costs[y][x] < cost:
            continue

        for k in range(4):
            ny,nx = y+dy[k], x+dx[k]

            if isOutOfBounds(ny,nx): continue

            newCost = cost + 1 if board[ny][nx] == 1 else cost

            if newCost < costs[ny][nx]:
                costs[ny][nx] = newCost
                heapq.heappush(heap, (newCost, ny,nx))

    return costs[e_y][e_x]

m,n = map(int, input().split())
board = [list(map(int,list(input()))) for _ in range(n)]
print(dijkstra(board, (0,0), (n-1,m-1)))
```

## 알게된 점
- 최단거리 문제를 풀 때 반드시 가중치 차이 여부를 먼저 고려하자.
- 유사한 문제 : [미로 만들기](https://www.acmicpc.net/problem/2665)
## 결과
|풀이|방식|시간|
|:---:|:---:|:--------:|
|1|BFS(단, 중복으로 방문 가능)|228 ms(pypy3), 시간 초과(python3)| 
|1|다익스트라|116 ms(python3)| 