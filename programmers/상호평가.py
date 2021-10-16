def solution(scores):
    n = len(scores)
    avgScore = []
    colScore = [[] for _ in range(n)]

    def filterScore(n):
        if n >= 90: return "A"
        if n >= 80: return "B"
        if n >= 70: return "C"
        if n >= 50: return "D"
        return "F"

    for i in range(n):
        for j in range(n):
            colScore[j].append(scores[i][j])

    for i, score in enumerate(colScore):
        _sum, _max, _min = sum(score), max(score), min(score)
        _maxCount = score.count(_max)
        _minCount = score.count(_min)

        if (score[i] == _max and _maxCount == 1) or (score[i] == _min and _minCount == 1):
            avgScore.append(((_sum - score[i]) / (n - 1)))
        else:
            avgScore.append((_sum / n))

    return ''.join((map(filterScore, avgScore)))