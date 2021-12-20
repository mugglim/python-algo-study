## 링크
https://www.acmicpc.net/problem/1062

## 설명
- 메모리 제한 때문에 비트 마스킹을 사용
- 백트랙킹을 통해 탐색 범위를 제한
- 자세한 흐름은 다음과 같다.
    1. 접두사 `anta`와 접미사 `tica`은 반드시 알아야만 하므로, 공통 단어 `antic`는 필수적으로 알아야 한다. -> k는 5이상 필요
    2. 단어에서 `a|n|t|i|c`은 제외한다. => 정규식 `/[antic]/g`
    3. 단어에서 사용되는 모든 문자를 set으로 관리하여 탐색 범위를 제한한다.
    4. dfs 시작.
        - 종료 조건 
            - 더 이상 문자를 탐색할 수 없는 경우 (cnt == 0)
            - A=단어, B=방문한 문자 라고 했을 때 len((A∩B)) == len(A) 인 경우만 카운팅
            - ans = max(ans, cnt)로 최대값 갱신
        - 재귀
            - 이전 index의 다음 문자 부터 loop를 돌려 탐색 범위 제한
## 풀이 1

```python
import sys
import re
input = lambda: sys.stdin.readline().rstrip()


def addBit(bit,i): return bit | (1 << i)
def removeBit(bit, i): return bit & ~(1 << i)
def isExistBit(bit, i): return bit & (1 << i)
def intersection(s1,s2): return s1 & s2
def replaceRequiredCh(s): return re.sub("[antic]", '', s)

def wordToBit(word):
    bit = 0
    for ch in replaceRequiredCh(word):
        bit = addBit(bit, ord(ch) - ord('a'))
    return bit


n,k = map(int,input().split())
words = [input() for _ in range(n)]

def solution(n,k, words):
    if k < 5: return 0
    if k == 26: return n
    ans = 0
    visited = 0

    for ch in set("antatica"): addBit(visited, ord(ch) - ord('a'))

    bitWords = [wordToBit(word) for word in words]
    requiredCh = list(set(''.join([replaceRequiredCh(word) for word in words])))

    if k - 5 >= len(requiredCh): return n

    def countKnowWord():
        nonlocal ans
        cnt = 0

        for bitWord in bitWords:
            if intersection(bitWord, visited) == bitWord: cnt += 1

        return cnt


    def dfs(cnt, l):
        nonlocal ans, visited

        if cnt == 0:
            ans = max(ans,countKnowWord())
            return

        for i, ch in enumerate(requiredCh[l:]):
            x = ord(ch) - ord('a')
            if not isExistBit(visited, x):
                visited = addBit(visited, x)
                dfs(cnt - 1, i + l)
                visited = removeBit(visited, x)

    dfs(k - 5, 0)
    return ans

print(solution(n,k,words))
```

## 알게된 점

## 결과
|풀이|방식|시간|
|:---:|:---:|:--------:|
|1|비트 마스킹|3868 ms(pypy: 520ms)| 