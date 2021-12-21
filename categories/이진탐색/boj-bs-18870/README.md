## 링크
https://www.acmicpc.net/problem/18870

## 설명
x축 위의 좌표를 정렬 후 **자신 보다 작은** 좌표의 개수를 구하면 된다.  
(단, 중복된 숫자는 하나로 카운팅한다.)

중복된 숫자를 포함시키기 않기 위해, 배열을 set으로 변환 후 정렬한다.

이후, 정답의 index를 보장하기 위해 기존의 배열을 loop 돌면서 이진탐색으로 target의 index를 구한 후 정답에 반영해주자.
(arr : sorted set, target: num)

```text
[1000,999,1000,999,1000,999]

1) set
[1000, 999]

2) sorting by asc
[999, 1000]

3) loop 
for target in [1000,999,1000,999,1000,999]: 
    binarySearch(sortedSet, target)
```


## 풀이 1
```python
from bisect import bisect_left

n = int(input())

arr = list(map(int,input().split()))
s = sorted(list(set(arr)))

ans = [bisect_left(s,target) for target in arr]

print(*ans)
```

## 알게된 점

## 결과
|풀이|방식|시간|
|:---:|:---:|:--------:|
|1|bisect + set|2332ms| 