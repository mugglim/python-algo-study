import bisect
def solution(info, query):
    answer = []

    lang = {"cpp":{},"java":{},"python":{}}
    lan = ["cpp","java","python"]
    tech = ["backend","frontend"]
    age = ["junior","senior"]
    menu = ["chicken","pizza"]

    for k in lang.keys():
        for t in tech:
            lang[k][t] = {}
            for a in age:
                lang[k][t][a] = {}
                for m in menu:
                    lang[k][t][a][m] = []

    for inf in info:
        l,t,a,m,c = inf.split(" ")
        lang[l][t][a][m].append(int(c))
        lang[l][t][a][m].sort()

    for q in query:
        cnt = 0
        l,t,a,m = q.split(" and ")
        m,score = m.split(" ")
        score = int(score)
        l = lan if l == "-" else [l]
        t = tech if t == "-" else [t]
        a = age if a == "-" else [a]
        m = menu if m == "-" else [m]

        for k1 in l:
            for k2 in t:
                for k3 in a:
                    for k4 in m:
                        if len(lang[k1][k2][k3][k4]) > 0:
                            left_index = bisect.bisect_left(lang[k1][k2][k3][k4],score)


                            # 만약 점수가
                            cnt += len(lang[k1][k2][k3][k4]) - left_index

        answer.append(cnt)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])