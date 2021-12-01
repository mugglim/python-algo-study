from itertools import combinations

def solution(orders, course):
    answer = []
    result = {i : {} for i in course}

    for order in orders:
        for i in course:
            for menu in list(combinations(order,i)):
                if "".join(sorted(menu)) not in result[len(menu)]:

                    result[len(menu)]["".join(sorted(menu))] = 1
                else:
                    result[len(menu)]["".join(sorted(menu))] += 1

    for k1 in result.keys():
        if result[k1]:
            max_v = max([v for v in result[k1].values()])
            for k2 in result[k1].keys():
                if max_v >= 2 and result[k1][k2] == max_v:
                    answer.append(k2)

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))