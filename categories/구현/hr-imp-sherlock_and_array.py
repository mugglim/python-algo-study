def balancedSums(arr):
    if len(arr) == 1: return "YES"
    _sum = 0
    prefix = [0]
    isBalanced = False

    for x in arr:
        _sum += x
        prefix.append(_sum)

    for i in range(len(arr)):
        l,r = 0,0
        prefixIdx = i + 1

        if i == 0: l,r = 0, prefix[-1] - prefix[prefixIdx]
        elif i == len(arr) -1: l,r = prefix[prefixIdx-1], 0
        else: l,r = prefix[prefixIdx-1], prefix[-1] - prefix[prefixIdx]

        print(i,l,r)

        if l == r:
            isBalanced = True
            break

    return "YES" if isBalanced else "NO"