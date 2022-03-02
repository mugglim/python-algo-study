def quick_sort(arr, s, e):
    if s >= e: return
    pivot, l, r = s, s + 1, e

    while l <= r:
        while l <= e and arr[l] <= arr[pivot]: l += 1
        while r > s and arr[r] >= arr[pivot]: r -= 1

        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
        else:
            arr[pivot], arr[r] = arr[r], arr[pivot]

    quick_sort(arr, s, r - 1)
    quick_sort(arr, r + 1, e)

arr = [3,7,6,1,10,4]
quick_sort(arr,0, len(arr)-1)

