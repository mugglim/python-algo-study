
def solution(files):
    answer = []
    for file in files:
        l = 0
        head, number, tail = "", "", ""
        is_find = False
        while l < len(file):
            if file[l].isdigit() == True:
                r = l+1
                while r < len(file) and file[r].isdigit() == True:
                    r += 1
                is_find = True
                head = file[:l]
                number = file[l:r]
                tail = file[r:]
                break
            else:
                l += 1
            if is_find == True:
                break

        answer.append((head,number,tail))

    answer.sort(key=lambda x:(x[0].lower(),int(x[1])))
    answer = ["".join(x) for x in answer]
    return answer


# solution(["foo9.txt","foo010bar020.zip","F-15"])
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])