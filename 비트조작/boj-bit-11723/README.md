## 링크
https://www.acmicpc.net/problem/11723

## 설명
- 비트 조작을 구현해야 하는 문제
- 

## 풀이 1
set을 사용하지 않고 시프트 연산자를 통해 비트 조작을 구현해서 품

```python
from sys import stdin
input = stdin.readline

class BitMask:
    def __init__(self, size):
        self.bit = 0
        self.size = size

    def add(self, idx): self.bit |= (1 << idx)
    def remove(self, idx): self.bit &= ~(1 << idx)
    def toggle(self, idx): self.bit ^= (1 << idx)
    def all(self): self.bit = (1 << self.size) - 1
    def empty(self): self.bit = 0
    def check(self, idx): return self.bit & (1 << idx) != 0


bitMask = BitMask(20)
m = int(input())

for _ in range(m):
    cmd, *v = input().split()
    v = int(v[0]) - 1 if v else v

    if cmd == "add": bitMask.add(v)
    if cmd == "remove": bitMask.remove(v)
    if cmd == "check": print(1 if bitMask.check(v) else 0)
    if cmd == "toggle": bitMask.toggle(v)
    if cmd == "all": bitMask.all()
    if cmd == "empty": bitMask.empty()


```


## 알게된 점
- `(1 << size) - 1`를 통한 꽉 찬 집합 구현

## 결과
|풀이|방식|시간|
|:---:|:---:|:--------:|
|1|시프트 연산자를 통한 구현|5188 ms| 