## 링크
https://www.acmicpc.net/problem/22232
## 풀이 

`파일명.확장자` 인풋값을 `[파일영,확장자]` 처럼 배열로 맵핑하고, 다중 조건을 이용해서 정렬을 구현하면 된다.

```python
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())

files = [input().split(".") for _ in range(n)]
extensions = set(input() for _ in range(m))

ans = sorted(files, key=lambda x:(x[0], not x[1] in extensions, x[1]))
for l in ans: print('.'.join(l))
```

## 알게된 점
- Boolean 값에서의 정렬 할 때 True가 더 큰 값으로 인식된다.(False < True)

```python
"""
[1,2,3,4,5]     

1) x < 3 map
[(1,True),(2,True),(3,False),(4,False),(5,False)] 

2) sorting (False < True)
[(3,False),(4,False),(5,False),(1,True),(2,True)] 

3) result
[3,4,5,1,2]
"""
arr = [1,2,3,4,5]
arr.sort(key=lambda x:x<3)  # [3,4,5,1,2]
```


## 결과
|풀이|방식|시간|
|:---:|:---:|:--------:|
|1|다중 조건 정렬 |1276 ms| 