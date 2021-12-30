import heapq
import re
def solution(word, pages):
    answer = []
    dic = {}

    for idx,page in enumerate(pages):
        page = page.lower()
        url = re.search('<meta property="og:url" content=(.+?)/>',page).group(0).split("content=")[1][:-2][1:-1]
        txt = re.findall(r"[a-zA-Z]+",page)

        tmp_score = [0,[],0,0]

        # 1. 기본점수
        for w in txt:
            if word.lower() == w.lower():
                tmp_score[0] += 1

        # 2. 외부 링크수
        for a in re.findall('<a href=(.+?)</a>',page):
            a = a.split(">")[0][1:-1]
            tmp_score[1].append(a)

        dic[url] = tmp_score


    # 3. 링크점수 계산
    for k in dic.keys():
        for url in dic[k][1]:
            if url in dic:
                dic[url][2] += dic[k][0] / len(dic[k][1])

    # 4. 매칭점수
    for idx,k in enumerate(dic.keys()):
        heapq.heappush(answer,(-(dic[k][0]+dic[k][2]),idx))



    return heapq.heappop(answer)[1]


print(solution("blind",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))