## 서로소 집합 
- 교집합이 없는 두 집합
- 예시 
    - {1,2}, {3,4} O
    - {1,2}, {2,3} X

## Union-Find
- **서로소 집합**을 표현하기 위해 사용되는 자료구조
- (1) Union : 두 원소 a,b가 속한 집합을 하나로 합치는 연산
- (2) Find : 특정 원소 a의 속한 집합(루트 노트)을 반환하는 연산


## 과정
0. 초기화 : 모든 노드의 루트 노드를 자신으로 설정한다.
1. Union 연산 
   1) 두 노드 A,B의 루트 노드 A', B'을 탐색
   2) A'와 B'의 번호가 큰 쪽에서 작은 쪽을 가리키게 설정(관행..)
2. 모든 Union 연산을 처리될 때 까지 1번 과정을 반복한다.

## 코드(경로)
```python
n = 10
parent = [x for x in range(n+1)]

def findParent(parent, x):
    # boundary condition : 부모 노드가 자기 자신이면 종료
    if parent[x] == x: return x
    return findParent(parent, parent[x])

def union(a,b):
    rootA = findParent(parent, a)
    rootB = findParent(parent, b)

    if rootA < rootB : parent[rootB] = rootA
    else: parent[rootA] = rootB
```

## 코드(경로 압축 고려)
- findParent 함수는 트리가 편향 된 경우 Signly Linked List 같이 탐색
    - 어차피 알고 싶은 건 루트 노드
    ```
    # O(n)
    1 <-- 2 <-- 3 <-- 4 <-- 5 <-- ..... <-- x
    union(x, x+1) => O(v)
    ```
- 해결 : findParent 함수를 진행할 때, parent에 루느 노트를 반영한다.
    ```python
    # O(logn)
    def findParent(parent, x):
        if parent[x] == x: return x
        
        # 재귀함수 종료 후, 루트 노트를 반영
        parent[x] = findParent(parent, parent[x])
        # 반영 된 루트노드를 반환
        return parent[x]
    ```

## 클래스
```python
class DS:
    def __init__(self, n):
        self.parent = [x for x in range(n+1)]

    def find(self, x):
        if self.parent[x] == x: return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX > rootY: self.parent[rootX] = rootY
        else: self.parent[rootY] = self.parent[rootX]
```





### ref
- [이코테 서로소 집합 자료구조](https://www.youtube.com/watch?v=Ha0w2dJa2Nk)
- [위키피디아 - 서로소 집합 자료 구조](https://ko.wikipedia.org/wiki/%EC%84%9C%EB%A1%9C%EC%86%8C_%EC%A7%91%ED%95%A9_%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0)