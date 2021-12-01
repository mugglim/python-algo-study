def twoPointer(arr, target):
    ans = -1
    l, r = 0, len(arr) -1

    while(l < r):
        total = a[l] + a[r]
        if total == target:
            ans = [l, r]
            break
        elif total < target:
            l += 1
        elif total > target:
            r -= 1

    return ans