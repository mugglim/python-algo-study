def mergeSort(arr):
    # 1) split
    if len(arr) == 1: return arr

    mid = len(arr) // 2

    leftArr, rightArr = arr[:mid], arr[mid:]
    sortedLeftArr, sortedRightArr = mergeSort(leftArr), mergeSort(rightArr)

    # 2) merge
    sortedArr = []
    l,r = 0,0

    while l < len(sortedLeftArr) or r < len(rightArr):
        # 1) 한 쪽 배열을 모두 탐색한 경우
        if l == len(sortedLeftArr):
            sortedArr.extend(sortedRightArr[r:])
            break
        if r == len(sortedRightArr):
            sortedArr.extend(sortedLeftArr[l:])
            break

        # 2) 어느 한 쪽 배열도 모두 탐색하지 않은 경우
        if sortedLeftArr[l] <= sortedRightArr[r]:
            sortedArr.append(sortedLeftArr[l])
            l += 1
        else:
            sortedArr.append(sortedRightArr[r])
            r += 1

    return sortedArr




