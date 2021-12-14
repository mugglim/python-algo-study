import bisect

# (1) without bisect
def bs(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target: return mid
        if arr[mid] < target: l = mid + 1
        elif arr[mid] > target: r = mid - 1

    return -1

# (2) with bisect
def binarySearch(arr, target):
    size = len(target)
    idx = bisect.bisect_left(arr, target)

    return 0 <= idx < size and arr[idx] == target


# (2-1) count by bisect
def countByBinarySearch(arr, target):
    l = bisect.bisect_left(arr,target)
    r = bisect.bisect_right(arr,target)
    return r - l


