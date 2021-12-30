def solution(record):
    answer = []
    dic = {}
    descript = {"Enter" : "님이 들어왔습니다.", "Leave" : "님이 나갔습니다."}
    for r in record:
        r = r.split(" ")
        if r[0] == "Enter":
            answer.append([r[1],r[0]])
            dic[r[1]] = r[2]
        elif r[0] == "Leave":
            answer.append([r[1], r[0]])
        elif r[0] == "Change":
            dic[r[1]] = r[2]

    answer = [dic[l[0]] + descript[l[1]] for l in answer]

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])