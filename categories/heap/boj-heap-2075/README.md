## 링크
https://www.acmicpc.net/problem/2075

## 풀이

최소 힙을 사용했으며 아이디어는 다음과 같다.
1. 최소 힙을 초기화한다.
2. row를 loop 돌면서 아래의 과정을 반복한다.
   - 경우1) 힙이 꽉 차지 않은 경우 
     - 값을 push한다.
   - 경우2) 힙이 꽉 찬 경우 and 값이 힙의 최소값(첫 번째 index값)보다 큰 경우
     - 힙을 pop 한다 (새로운 값을 넣기 위한 공간 확보)
     - 값을 push한다.
3. 최소 힙의 첫 번째 원소를 반환한다.(== n번째 큰 수)
```python
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

minHeap = []
n = int(input())

for i in range(n):
    row = list(map(int,input().split()))
    for x in row:
        if len(minHeap) < n: heapq.heappush(minHeap, x)
        else:
            if minHeap[0] < x:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, x)

print(minHeap[0])
```

## 결과
|  풀이   |   방식   |    시간     |
|:-----:|:------:|:---------:|
|   1   |  최소 힙  |  1164 ms  | 