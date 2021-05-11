import re
from datetime import timedelta
from collections import Counter

def solution(m, musicinfos):
    answer = []
    shart_alpha = ["C","D","F","G","A"]
    for order,musicinfo in enumerate(musicinfos):
        minutes = 0
        
        # 데이터 전처리
        musicinfo = musicinfo.split(",")
        h_start, h_end = int(musicinfo[0][:2]), int(musicinfo[1][:2])
        m_start, m_end = int(musicinfo[0][3:]), int(musicinfo[1][3:])

        s = timedelta(hours=h_start,minutes=m_start)
        e = timedelta(hours=h_end,minutes=m_end)

        h,min,s = str((e-s)).split(":")

        minutes = int(h)*60 + int(min)

        sharp_count = 0
        counter = Counter(musicinfo[3])
        if "#" in counter:
            sharp_count += counter["#"]

        song_length = len(musicinfo[3]) - sharp_count

        song = (minutes // song_length) * musicinfo[3] + musicinfo[3][:minutes%song_length]

        idx_list = [m.start() for m in re.finditer(m,song)]
        for idx in idx_list:
            last_ch = song[idx + len(m) -1]
            if idx + len(m) == len(song):
                answer.append((minutes,order,musicinfo[2]))
            elif idx + len(m) < len(song):
                if last_ch != "#" and last_ch in shart_alpha and song[idx + len(m)] == "#":
                    continue
                answer.append((minutes, order, musicinfo[2]))



    if len(answer) == 0:
        return "(None)"
    else:
        return sorted(answer,key=lambda x:(-x[0],x[1]))[0][-1]

# print(solution("CCB",["12:00,12:03,Hello,CCB#"]))
# print(solution("A#G",["12:00,12:03,Hello,A#G#"]))