def solution(gems):
    # 맨 앞애 있는 녀석이 2개 이상이면 맨앞에 녀석을 뺀다.

    jewel_set = set(gems)
    size = len(jewel_set)

    # 투포인터로 풀이한다.
    start = 0
    end = 0
    jewel_dict = {}  # 빈도수를 저장한다.
    answer = []  # 가능한 [시작: 끝] 리스트를 담는다.

    # end가 gems의 길이와 같으면 탈출한다.
    while end != len(gems):

        # 만약 최소 1개이상 포함한다면, 그 구간은 answer에 포함한다.
        if len(jewel_dict) == size:
            answer.append([start + 1, end])

        # 한번도 구매안한 보석이면 구매한다.
        if jewel_dict.get(gems[end]) == None:
            jewel_dict[gems[end]] = 1
            end += 1
        # 구매 이력이 있다면
        else:
            jewel_dict[gems[end]] += 1
            # end와 start가 같은 보석인지를 확인한다.(만약 같으면 start쪽 보석은 빼도 무방하다.이미 뒤에 하나 있으니까)
            if gems[start] == gems[end]:
                while jewel_dict[gems[start]] > 1:  # start 보석이 빈도수가 2이상이면 하나 빼도 된다. 이렇게 빈도수를 최소한으로 줄인다.
                    jewel_dict[gems[start]] -= 1
                    start += 1
            end += 1
        # print(gems[start:end + 1])

    # 마지막에 최소 하나씩 포함하는 구간을 포함해준다.
    if len(jewel_dict) == size:
        answer.append([start + 1, end])

    answer = sorted(answer, key=lambda x: (x[1] - x[0], x[0]))
    # print(answer)
    return answer[0]
