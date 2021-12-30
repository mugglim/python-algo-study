## 링크
https://www.acmicpc.net/problem/20040

## 설명

> C에 속한 임의의 선분의 한 끝점에서 출발하여 모든 선분을 한 번씩만 지나서 출발점으로 되돌아올 수 있다.  
> 이 중 어느 세 점도 일직선 위에 놓이지 않는다.

즉, 정점을 연결하면서 최초로 사이클이 발생한 시점을 반환해주면 된다.

## 풀이 
```python
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
ans = 0

def find(x):
    if parent[x] == x: return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    rootX = find(x)
    rootY = find(y)

    if rootX == rootY: return True

    if rootX < rootY: parent[rootY] = rootX
    else: parent[rootX] = rootY

for i in range(m):
    x,y = map(int,input().split())
    if union(x,y):
        ans = i + 1
        break

print(ans)
```

## 결과
|풀이|방식|시간|
|:---:|:---:|:--------:|
|1|유니온 파인드 |884 ms| 