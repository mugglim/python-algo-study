## 링크
https://www.acmicpc.net/problem/22233

## 풀이 

1. n개의 키워드 단어를 set으로 저장해둔다.  
2. m개의 입력이 들어오는데, 매번 입력마다 쉼표(,)를 기준으로 사용한 단어 목록을 파싱한다.  
3. 2번 과정에서 파싱한 단어 목록 중 키워드에 해당하는 단어가 있다면 키워드에서 해당 단어를 지워준다.
4. 3번 과정 이후, 키워드의 개수를 확인한다.

```python
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
keywords = set(input() for _ in range(n))
ans = []

for _ in range(m):
    words = input().split(",")
    for word in words:
        if word in keywords: keywords.remove(word)

    ans.append(len(keywords))


for x in ans: print(x)
```

## 결과
|풀이|방식|시간|
|:---:|:---:|:--------:|
|1|set|968 ms| 