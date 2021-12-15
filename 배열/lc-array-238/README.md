## 링크
https://leetcode.com/problems/product-of-array-except-self/

## 생각
- 1차
    - 좌측, 우측 prefix를 두 개 만들어 자신을 제외한 값을 곱해주면 되지 않을까? 
- 2차
    - 0이 2개 이상이면, 모든 경우의 곱은 0이다. 바로 return 가능
    - 0이 1개인 경우, 0인 경우만 0을 제외한 곱을 반영해주면 된다.
    - 0이 0개인 경우는 누적합과 유사하게 풀면 됨.
## 결과

|답안|시간|설명|통과 여부|
|---|---|---|--------|
|1차|369ms|두 개의 prefix|O| 
|2차|300ms|prefix를 사용하지 않음|O| 



## 코드

### 1차
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = [1,1]
        prefix = [[0], [0]]
        output = []
        
        for i in range(len(nums)):
            total[0] *= nums[i]
            total[1] *= nums[-1-i]
            
            prefix[0].append(total[0])
            prefix[1].append(total[1])
        
        
        for i in range(len(nums)):
            if i == 0: output.append(prefix[1][-i-2])
            elif i == len(nums) -1: output.append(prefix[0][i])
            else: output.append(prefix[0][i] * prefix[1][-i-2])
                
        
        return output
```

### 2차
```python
class Solution:    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        total = nums[0]
        answer = []
        
        for x in nums[1:]: 
            if x!= 0: total *= x
            else: zero_cnt += 1
        
        if zero_cnt > 1: return [0] * len(nums)
        
        for x in nums:
            if zero_cnt == 1:
                if x == 0: answer.append(total)
                else: answer.append(0)
            else:
                answer.append(total // x)
        
        return answer
```