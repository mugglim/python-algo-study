def solution(m, musicinfos):
    answer = []
    for i,musicinfo in enumerate(musicinfos):

        music = musicinfo.split(",")
        start = [int(music[0][:2]),int(music[0][3:])]
        end = [int(music[1][:2]),int(music[1][3:])]
        name = music[2]
        melody = music[3]


        j= 0
        new_melody = []
        while j < len(melody) -1:
            if melody[j + 1] == "#":
                new_melody.append(f"{melody[j]}#")
                j += 2
            else:
                new_melody.append(melody[j])
                j += 1
                # 마지막을 고려
            if j == len(melody) - 1:
                new_melody.append(melody[j])






        total_time = 0

        # 시작시간과 끝나는 시각이 같은 경우
        if start[0] == end[0]:
            total_time =  end[1] - start[1]
        else:
            # 시작시간과 끝나는 시간이 다른 경우
            # 12:11 ~ 13:55
            # 12:01 ~ 14:00
            for hour in range(start[0],end[0]+1):
                if hour == start[0]: # 시작 시간을 고려
                    total_time += 60 - start[1]
                elif hour == end[0]: # 끝나는 시각을 고려
                    total_time += end[1]
                else:
                    total_time += 60

        str_new_melody = "".join(new_melody)

        # 재생 된 멜로디
        # total time = 3, melody_length = 3,
        total_melody = (total_time // len(new_melody)) * str_new_melody + "".join(new_melody[:total_time % len(new_melody)])


        print(total_melody,len(total_melody))
        # 만약 기억한 멜로디가 재생된 멜로디 안에 있다면?
        while 1:
            if m not in total_melody:
                break
            else:
                index = total_melody.index(m) # 멜로디가 시작된 부분
                # index를 지속적으로 변화하기
                if index + len(m) == len(total_melody)or \
                        (index + len(m) < len(total_melody) and total_melody[index + len(m)]) != "#":
                    answer.append([total_time, i, name])
                    break
                elif index + len(m) < len(total_melody) and total_melody[index + len(m)] == "#":
                    total_melody = total_melody[index+len(m)+1:]




    if answer:
        # x[0] : 재생시간, x[1] : 들어온 순서, x[2] : 노래 제목
        return sorted(answer,key=lambda x:(-x[0],x[1]))[0][2]
    else:
        return "(None)"

# 반례입니당

print(solution("E#B",["13:50,14:00,Hello,CE#B#"]))
# print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CCB",["12:00,12:03,Hello,CCB#"]))
# print(solution("CCB",["12:00,12:03,Hello,A#B#"]))