def rateFilter(s):
    if s == "N": return 0
    if s == "W": return 1
    if s == "L": return -1


def rateToNum(stat):
    return list(map(rateFilter, stat))


def getWinRate(numStat):
    filterdStat = list(filter(lambda x: True if x != 0 else False, numStat))
    winCount = numStat.count(1)
    result = 0 if len(filterdStat) == 0 or winCount == 0 else winCount / len(filterdStat)
    return result


def getWinCountOverWeight(weights, numStats):
    result = []

    for i, numStat in enumerate(numStats):
        cnt = 0
        for j, stat in enumerate(numStat):
            if i == j: continue
            if stat == 1 and weights[i] < weights[j]: cnt += 1
        result.append(cnt)
    return result


def solution(weights, head2head):
    n = len(weights)
    answer = [i for i in range(1, n + 1)]
    numStats = [rateToNum(stat) for stat in head2head]
    winRates = [getWinRate(numStat) for numStat in numStats]
    winCountsOverWeight = getWinCountOverWeight(weights, numStats)

    answer.sort(key=lambda idx: (
        -winRates[idx - 1],
        -winCountsOverWeight[idx - 1],
        -weights[idx - 1],
        idx
    )
                )
    return answer