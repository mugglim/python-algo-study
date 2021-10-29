# Two Pointer

- 정렬된 Array에서 특정 조건을 만족하는 두 원소를 찾기 위함.
- Big-O` : O(n)


```python
def twoPointer(arr, target):
    ans = -1
    left, right = 0, len(arr) -1

    while(left < right):
        total = a[left] + a[right]
        if total == target:
            ans = [left, right]
            break
        elif total < target:
            left += 1
        elif total > target:
            right -= 1

    return ans
```
