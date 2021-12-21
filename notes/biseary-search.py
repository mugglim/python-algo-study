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


def lower_bound(arr,target):
    l,r = 0, len(arr) - 1

    while l <= r:
        mid = (l+r) // 2
        if arr[mid] < target: l = mid + 1
        else: r = mid

    return r+1


def upper_bound(arr,target):
    l,r = 0, len(arr) - 1

    while l <= r:
        mid = (l+r) // 2
        if arr[mid] <= target: l = mid + 1
        else: r = mid

    return r+1

# (2) with bisect
# bisect_left(arr, target, lo=0, hi=len(arr))
# bisect_right(arr, target, lo=0, hi=len(arr))
#   (1) lo를 통해 탐색 시작 범위를 설정할 수 있음.
#   (2) hi를 통해 탐색 종료 범위를 설정할 수 있음.
def binarySearch(arr, target):
    size = len(target)
    idx = bisect.bisect_left(arr, target)

    return 0 <= idx < size and arr[idx] == target


# (2-1) count by bisect
def countByBinarySearch(arr, target):
    l = bisect.bisect_left(arr,target)
    r = bisect.bisect_right(arr,target)
    return r - l


