## 링크
https://www.acmicpc.net/problem/2473

## 풀이 1

이전에 푼 [용액](https://www.acmicpc.net/problem/2467) 문제와 비슷 하다고 생각했다.
하나의 값을 고정하고, 나머지 영역을 투 포인터를 돌렸다. 그런데, 띠용. TEL를 받았다.(단, pypy3는 통과)   

잘 풀리지 않아 해법을 찾아보던 중, `parametric search`을 적용하면 된다고 한다.
이후에 다시 최적화하여 python으로 AC를 받아보자.

[parametric search 강의 링크](https://www.youtube.com/watch?v=3TkaOKHxHnI)

```python
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().split())))
ans = None

i = 0

while i < n - 2:
    j,k = i+1, n-1

    while j < k:
        tot = arr[i] + arr[j] + arr[k]

        if not ans or abs(tot) < abs(sum(ans)): ans = [arr[idx] for idx in [i,j,k]]

        if tot > 0: k -= 1
        else: j += 1
    i += 1

print(*ans)
```

## 결과
|풀이|     방식     |             시간              |
|:---:|:----------:|:---------------------------:|
|1| 정렬 + 투포인터  | TLE(python), 1000 ms(pypy3) | 