## 링크
https://www.acmicpc.net/problem/1976
## 생각
- 여행 경로의 노드의 루트 노드가 다르면 여행이 불가하다.
- 연결 된 도시에 대해서 union 연산을 수행한다.
- union(1,3)은 union(3,1)과 동일하므로 중복 된 연산은 제외해야 하는데...
    - 어차피 O(1)에 처리 가능하다. 이후에 최적화 해보자
- union-find 이후 집합의 개수가 2개 이상이면 cycle이 발생하지 않은 것 이므로, 여행이 불가하다.

## 결과

|답안|시간|설명|통과 여부|
|---|---|---|-------|
|1차|76 ms|union-find |O| 


## 코드
```python
import sys
input = sys.stdin.readline

class DS:
    def __init__(self, n):
        self.parent = [x for x in range(n + 1)]

    def find(self, x):
        if self.parent[x] == x: return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX < rootY: self.parent[rootY] = rootX
        else: self.parent[rootX] = rootY

def main():
    n = int(input())
    m = int(input())

    graph = [list(map(int,input().split())) for _ in range(n)]
    trace = list(map(int,input().split()))


    ds = DS(n)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1: ds.union(i + 1,j + 1)

    parent = ds.parent
    parentKinds = [parent[x] for x in trace]

    return len(set(parentKinds)) == 1

if __name__ == "__main__":
    ans = main()
    print("YES" if ans else "NO")
```
