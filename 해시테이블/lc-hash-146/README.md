## 링크
https://leetcode.com/problems/lru-cache/submissions/

## 설명
- LRUCache를 위한 자료구조를 디자인한다.
- get 메소드
    - key 있는 경우 페이지를 최신화 하고 value 반환
    - 없는 경우 -1 반환
- put 메소드
    - key 있는 경우 페이지 최신화 
    - 없는 경우 key 반영  
    (단, 캐시 용량이 꽉 찬 경우, 가장 사용한 지 오래된 페이지를 제거한다.)
        
## 풀이 1(default dict + iterator)
dict는 입력 순서를 보장한다. (> Python 3.6)   
그렇기에, 가장 첫 번째 key 값을 오래된 페이지 값으로 생각하였다.

```python
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    # 기본으로 구현해야 하는 메소드
    def get(self, key: int) -> int:
        if key in self.cache:
            self.update(key, self.cache[key])
            return self.cache[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: self.update(key, value)
        else:
            if self.isFull(): self.popLeft()
            self.cache[key] = value

    #  추가로 구현한 메소드
    def update(self, key, value):
        del self.cache[key]
        self.cache[key] = value

    def popLeft(self):
        k = next(iter(self.cache))
        del self.cache[k]

    def isFull(self):
        return len(self.cache) == self.capacity
```

## 알게된 점
- iter(iterable) 함수를 통해 iterator를 반환 받을 수 있다. O(1)
```python
arr = [1,2,3,4,5]
it = iter(arr)
print(next(it)) # 1
```
## 결과

|풀이|방식|시간|
|:---:|:---:|:--------:|
|1|default dict + iterator|966ms| 