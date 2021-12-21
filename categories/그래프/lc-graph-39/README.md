### 설명

|답안|시간|생각|통과 여부|
|:---:|:---:|:---|:--------:|
|1차|649 ms|중복을 방지하기 위해 dic를 두고, tuple로 key값으로 설정하자.|O|
|2차|211 ms|1차 시도에 추가로, candidates을 정렬 + 오른쪽 탐색범위 제한(`curr + x > target: break`)|O|
|3차|102 ms|2차 시도에 추가로, stack로 visited 제거 및 leftPivot을 두어 왼쪽 탐색범위 제한|O|

### 답안 코드

####  1차 답안
- 중복을 방지하기 위해 dic를 두고, tuple로 key값으로 설정하자.
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = {}

        def dfs(curr=0, visited=[]):
            nonlocal result
            if curr == target:
                visitedKey = tuple(visited)
                result[visitedKey] = True

            for x in candidates:
                nextVisited = sorted([*visited, x])
                nextVisitedKey = tuple(nextVisited)

                if curr + x <= target and nextVisitedKey not in result: dfs(curr + x, nextVisited)

        dfs()

        return [list(x) for x in result.keys()]
```

#### 2차 답안
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = {}
        candidates.sort()

        def dfs(curr=0, visited=[]):
            nonlocal result
            if curr == target:
                visitedKey = tuple(visited)
                result[visitedKey] = True

            for x in candidates:
                nextVisited = sorted([*visited, x])
                nextVisitedKey = tuple(nextVisited)

                if curr + x > target: break

                if nextVisitedKey not in result:
                    dfs(curr + x, nextVisited)

        dfs()

        return [list(x) for x in result.keys()]
```

#### 3차 답안
```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        stack = []
        arr = sorted(candidates)

        def dfs(curr = 0, leftPivot = 0):
            if curr == target:
                result.append([*stack])
                return

            for x in arr:
                if curr + x > target: break

                if x - leftPivot >= 0:
                    stack.append(x)
                    dfs(curr + x, x)
                    stack.pop()


        dfs()
        return result
```