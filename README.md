#  🔥 알고리즘 공부방

알고리즘을 문제 풀이 저장소입니다. 👊👊

### BOJ Profile
<img align='center' src="http://mazassumnida.wtf/api/v2/generate_badge?boj=mugglim">

### Commit 
```python
programmers : 'pg-category-name'
backjoon : 'boj-category-name'
leetcode : 'lt-category-name'
hackerrank : 'hr-category-name'
```

### 귀찮은 인덱싱은 그마아안!
```python
# nope!
a,b,c,d = map(int,input().split())
a,b,c,d, = a-1, b-1,c-1,d-1

# yes!
a,b,c,d = map(lambda x:x-1, map(int,input().split()))
```

### Reduce
```python
from functools import reduce

# map의 return 값은 객체이다.
# reduce는 초기값을 설정할 수 있다.

nums = [1,2,3,4,5,6,10]
arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
objList = [
    {'name': "박지성", 'team': "맨유"},
    {'name': "손흥민", 'team': "토트넘"},
    {'name': "황희찬", 'team': "울버햄튼"},
]

# sum
print(reduce(lambda x,y: x+y, nums)) # 31
print(reduce(lambda x,y: x+y, nums,10)) # 41
print(reduce(lambda x,y: x+y, nums,100)) # 131


# 2d -> 1d
print(reduce(lambda prev, next: [*prev, *next], arr1))
# 초기값을 선언하는 경우
print(reduce(lambda prev, next: [*prev, *next], arr1,[]))


# obj -> string
print(list(map(lambda obj: f"이름:{obj['name']}, 팀:{obj['team']}",objList)))
```


### Two Pointer
```python
def twoPointer(arr, target):
    ans = -1
    left, right = 0, len(arr) -1

    while(left < right):
        total = a[left] + a[right]
        if total == target:
            ans = [left, right]
            break
        elif total < target:
            left += 1
        elif total > target:
            right -= 1

    return ans
```

### BFS
```python
from collections import deque


def bfs(graph, start_vertex):
    queue = deque([start_vertex])
    answer = []
    visited = {}
    visited[start_vertex] = True
    answer.append(start_vertex)

    while queue:
        curr = queue.popleft()
        for _next in graph[curr]:
            if _next not in visited:
                visited[_next] = True
                queue.append(_next)
                answer.append(_next)

    return answer
```

### DFS 
- (1), (2)은 동일한 결과를 반환한다.
```python

def dfs(value, visited):
    # bad
    for _next in graph[value]:    
        # (1)
        if  not in visited: 
            visited.append(value)
            dfs(_next, visited)
            visited.pop()
        # (2)
        if  not in visited: 
            dfs(_next, [*visited, _next])   

dfs(0, [])
```

## Shorted-Path

### Dijkstra 
```python
def dijkstra(graph,start,end):
    n = len(graph)
    costs = [INF] * n
    heap = [(0, start)]
    costs[start] = 0

    while heap:
        cost, currentVertex = heapq.heappop(heap)

        if costs[currentVertex] < cost:
            continue

        for l in graph[currentVertex]:
            nextVertex, nextCost = l
            newCost = cost + nextCost

            if newCost < costs[nextVertex]:
                costs[nextVertex] = newCost
                heapq.heappush(heap, (newCost, nextVertex))

    return costs[end]
```

### Floyd-Warshall
```python
def floyd(n,graph):
    costs = [[INF] * n for _ in range(n)]

    for i in range(n): costs[i][i] = 0

    for k in range(n):
        for a in range(n):
            for b in range(n):
                costs[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    return costs
```