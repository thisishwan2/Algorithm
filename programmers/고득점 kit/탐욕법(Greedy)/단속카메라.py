def solution(routes):
    answer = 0
    dp = [0] * 600000

    # 정렬해야. 비교하기 쉽다.
    routes = sorted(routes, key=lambda x: (x[0], x[1]))
    # print(routes)
    now = routes[0]
    cnt = 1

    for i in range(1, len(routes)):
        if now[1] >= routes[i][1]:  # 다음 진출 위치가 이전 진출 위치보다 작으면 겹치는 부분이 존재함. now 갱신
            now = routes[i]
        elif now[1] > routes[i][0]:  # 다음 진입 위치가 이전 진출 위치보다 작으면, 겹치는 부분이 존재함. now 갱신(다음 진입 위치, 이전 진출 위치)
            now = [routes[i][0], now[1]]
        elif now[1] < routes[i][0]:  # 다음 진입 위치가 이전 진출 위치보다 크면, 겹치는 부분 x
            cnt += 1
            now = routes[i]

    # print(cnt)

    return cnt