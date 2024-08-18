def solution(storey):
    answer = 0
    while True:
        if storey == 0:
            break
        num = storey % 10
        n_num = (storey // 10) % 10

        # 테스트 해볼 케이스 199, 101, 1001, 1555, 12345678, 95

        # 만약 현재 자리값이 0이면 마법의 돌을 쓰지 않아도 된다.
        if num == 0:
            storey = storey // 10
        # 만약 5보다 크거나, 5인 경우에 다음 자리값이 5보다 크면 10으로 향하도록 마법의 돌을 쓴다.
        elif num > 5 or num == 5 and n_num >= 5:
            answer += 10 - num
            storey = storey // 10 + 1
        # 그게 아니고, 현재 자리값이 5보다 작거나, 5인데, 다음 자리값이 5보다 작으면 0으로 향한다.
        else:
            answer += num
            storey = storey // 10
        # print(storey)

    return answer