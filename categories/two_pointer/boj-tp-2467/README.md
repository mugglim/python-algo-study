## 링크
https://www.acmicpc.net/problem/2467

## 풀이 

주어진 용액에서 두 용액을 혼합 시 가장 0에 가까운 두 용액을 구하는 문제
단, 용액을이 오름차순으로 정렬되어 주어진다. 이러한 문제들은 **투 포인터**를 통해 O(N)에 해결 가능하다.

투 포인터의 조건을 다음과 같이 설정하였다.
1. 배열의 시작, 끝을 포인팅 한다. (l = 0, r = len(arr) - 1)
2. 두 용액의 합이 0보다 크다면, 오른쪽 포인터를 왼쪽으로 이동시켜 두 용액의 합을 감소시킨다. 
3. 두 용액의 합이 0보다 작거나 같다면, 왼쪽 포인터를 오른쪽으로 이동시켜 두 용액의 합을 증가시킨다.

### Ex.

```text
arr = [-99, -2, -1, 4, 98]

step    -99 -2  -1  4  98      diff
1       l               r      -1 < 0
2           l           r      96 > 0
3           l       r          2 > 0
4           l   r              -3 < 0
5              (l,r)           finish
 
```

### code
```python
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ans = None

l,r = 0, n -1

while l < r:
    diff = arr[r] + arr[l]
    if not ans or abs(diff) < abs(sum(ans)): ans = [arr[l], arr[r]]

    if diff > 0: r-=1
    else: l += 1

print(*ans)
```


## 결과
|풀이|   방식   |시간|
|:---:|:------:|:-------:|
|1| 투 포인터  |146 ms| 