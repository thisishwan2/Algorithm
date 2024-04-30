def solution(id_list, report, k):  # 이용자 배열, 이용자가 신고한 이용자 배열, 정지 기준

    user_dict = {}
    user_count_dict = {}
    for i in id_list:
        user_dict[i] = []
        user_count_dict[i] = 0

    for i, val in enumerate(report):
        user_id = val.split(" ")
        reporter_id = user_id[0]
        reported_id = user_id[1]

        if reported_id not in user_dict[reporter_id]:
            user_dict[reporter_id].append(reported_id)

    print(user_dict)

    tmp = []
    for i in user_dict.values():
        tmp = tmp + i
    # print(tmp)

    report = set([])
    for i in tmp:
        user_count_dict[i] += 1
        if user_count_dict[i] == k:
            report.add(i)

    # print(list(report))
    report = list(report)

    answer = []
    for i in user_dict.values():
        cnt = 0
        for j in i:
            if j in report:
                cnt += 1
        answer.append(cnt)
    return answer


'''
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list} # 해당 유저를 신고한 ID
    for i in set(report):
        i = i.split()
        dic_report[i[1]].append(i[0])
    print(dic_report)
    
    
    for key, value in dic_report.items():
        if len(value) >= k: # 2명이상이 신고했으면,
            for j in value: # 각 유저의 인덱스에 1을 더해준다.
                answer[id_list.index(j)] += 1

    return answer

'''