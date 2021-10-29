# Graph Search

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

