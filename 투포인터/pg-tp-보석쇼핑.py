def solution(gems):
    kinds = len(set(gems))
    length = len(gems)
    dic = {}
    ans = None
    r = 0

    def addJewelry(jewelry):
        if jewelry not in dic: dic[jewelry] = 0
        dic[jewelry] += 1

    def removeJewelry(jewelry):
        if dic[jewelry] - 1 == 0:
            del dic[jewelry]
        else:
            dic[jewelry] -= 1

    for l in range(length):
        while r < length and len(dic) < kinds:
            addJewelry(gems[r])
            r += 1

        if not ans or (len(dic) == kinds and (ans[1] - ans[0] > r - l - 1)):
            ans = [l + 1, r]

        removeJewelry(gems[l])

    return ans
