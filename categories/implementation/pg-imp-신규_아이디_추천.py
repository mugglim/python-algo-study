def solution(new_id):
    # 1단계
    new_id = "".join([x.lower() if x.isupper() else x for x in new_id])
    # 2단계
    new_id = "".join([x for x in new_id  if x.isalpha() or x.isdigit() or x == "-" or x =="." or x == "_"])
    # 3단계
    is_find = False
    tmp = ""
    for x in new_id:
        if x == "." and is_find == True:
            continue
        elif x == "." and is_find == False:
            tmp += "."
            is_find = True
        elif x != ".":
            tmp += x
            is_find = False
    new_id = tmp

    if new_id[0] == "." and new_id[-1] != ".":
        new_id = new_id[1:]
    elif new_id[0] != "." and new_id[-1] == ".":
        new_id = new_id[:-1]
    elif new_id[0] == "." and new_id[-1] == ".":
        new_id = new_id[1:-1]

    # 5단계
    if len(new_id) == 0:
        new_id = "a"

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]

    return new_id

print(solution("=.="))