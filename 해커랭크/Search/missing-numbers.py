def getCountList(arr):
    dic = {}
    for x in arr:
        if x not in dic: dic[x] = 1
        else: dic[x] += 1
    return dic


def missingNumbers(arr, brr):
    answer = []

    arrCounter = getCountList(arr)
    brrCounter = getCountList(brr)

    print(arrCounter, brrCounter)


    for k,v in arrCounter.items():
        if k in brrCounter and v != brrCounter[k]:
            answer.append(k)
            del brrCounter[k]
        elif k not in brrCounter:
            answer.append(k)

    for k,v in brrCounter.items():
        if k in arrCounter and v != arrCounter[k]:
            answer.append(k)
        elif k not in arrCounter:
            answer.append(k)

    return sorted(answer)
