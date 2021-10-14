def solution(files):
    answer = []
    head, number, tail = "", "", ""
    for file in files:
        index = 0

        # 숫자 시작 구하기
        # 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로

        for i, x in enumerate(file):
            if x.isalpha() == False and x != "-" and x != "." and x != " ":
                index = i
                break

        r = index + 1

        # Number 종료 끝내기
        cnt = 0  # 최대 숫자는 5자리이다.
        while r < len(file):
            if cnt == 4:  # base case
                break
            if file[r].isalpha() == False and file[r] != "-" and file[r] != "." and file[r] != " ":
                r += 1
                cnt += 1
            else:
                break

        head, number, tail = file[:index], file[index:r], file[r:]
        print(head, number, tail)
        answer.append([head, number, tail])

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return ["".join(x) for x in answer]

# print(solution(["abc123defg123.jpg"]))
#
# print(solution(["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"]))
# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))