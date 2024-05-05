# 해설
# 1. C#,D#,F# 등을 c,d,f와 같이 쓰이지 않는 문자로 치환해서 비교해도 된다.
# 2. ABC#을 [A,B,C#]과 같이 변환해서 배열을 비교하면서 풀어도 된다.


def solution(m, musicinfos):  # m: 네오가 기억한 멜로디, musicinfos: 방송된 곡의 정보

    # musicinfos는 [음악 시작 시각, 끝 시각, 음악제목, 악보정보]

    # #은 붙혀서 적어야함
    res = []
    m_list = []
    for i in range(len(m) - 1):
        if m[i] != "#" and m[i + 1] == "#":
            m_list.append(m[i] + m[i + 1])
        elif m[i] != "#" and m[i + 1] != "#":
            m_list.append(m[i])
        elif m[i] == "#":
            continue
    if m[-1] != "#":
        m_list.append(m[-1])
    print(m_list)

    answer = ''
    for index, i in enumerate(musicinfos):

        num = index

        info = i.split(",")

        start = info[0]
        end = info[1]
        name = info[2]
        melody = info[3]

        melody_list = list(melody)

        # #은 붙혀서 적어야함
        new_melody_list = []
        for j in range(len(melody_list) - 1):
            if melody_list[j] != "#" and melody_list[j + 1] == "#":
                new_melody_list.append(melody_list[j] + melody_list[j + 1])
            elif melody_list[j] != "#" and melody_list[j + 1] != "#":
                new_melody_list.append(melody_list[j])
            elif melody_list[j] == "#":
                continue
        if melody_list[-1] != "#":
            new_melody_list.append(melody_list[-1])
        print(new_melody_list)

        # 재생시간만큼 melody를 늘린다.
        end_time, end_min = end.split(":")
        start_time, start_min = start.split(":")

        end_minute = int(end_time) * 60 + int(end_min)
        start_minute = int(start_time) * 60 + int(start_min)

        running_time = end_minute - start_minute
        print(running_time)

        # 실제 재생 배열 생성
        if len(new_melody_list) >= running_time:
            run_melody = new_melody_list[:running_time]
        else:
            repeat = running_time // len(new_melody_list)
            plus = running_time % len(new_melody_list)

            run_melody = new_melody_list * repeat
            if plus != 0:
                run_melody = run_melody + new_melody_list[:plus]

        print(run_melody)

        # # 으로 인해 문자열의 find 메서드로 비교가 불가능
        for j, j_val in enumerate(run_melody):
            idx = j
            count = 0
            for k, k_val in enumerate(m_list):
                if idx < len(run_melody):
                    if run_melody[idx] == k_val:
                        idx += 1
                        count += 1

            # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다.
            # 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
            if count == len(m_list):
                res.append([len(run_melody), num, name])
                break

    # 만약 결과가 2개이상이면, 문제의 조건에 따라 가장 긴 러닝타임, 가장 먼저 입력된 음악 제목을 반환
    if len(res) > 1:
        res = sorted(res, key=lambda x: (-x[0], x[1]))
        print(res)
        return res[0][2]
    elif len(res) == 1:
        return res[0][2]
    return "(None)"