def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2) # 스테이지 정보
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])  # 스테이지에 도달한 사람 수
        yet = info[i + 1]  # 스테이지에 도달했으나 클리어 하지 못한 사람 수

        # 스테이지에 도달한 유저가 없는 경우
        if be == 0:
            fail.append([i + 1, 0])
        else:
            fail.append([i + 1, yet / be])

    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer


def solution(N, stages):
    answer = []

    dict_clear = {}
    dict_dodal = {}

    for i in range(1, N + 1):
        dict_clear[i] = 0
        dict_dodal[i] = 0

        for j in stages:
            if j > i:
                dict_dodal[i] += 1

            elif j == i:
                dict_clear[i] += 1
                dict_dodal[i] += 1
    print(dict_clear)
    print(dict_dodal)

    for i in range(1, N + 1):
        if dict_dodal[i] == 0:
            answer.append([0, i])
        else:
            answer.append([dict_clear[i] / dict_dodal[i], i])

    answer = sorted(answer, reverse=True)
    answer = sorted(answer, key=lambda answer: (-answer[0], answer[1]))

    res = []

    for i in answer:
        res.append(i[1])

    return res