from collections import deque


def solution(plans):
    answer = []

    new_plans = []
    # 문자열로 이루어진 시간을 분으로 바꾼다.
    for plan in plans:
        h, m = plan[1].split(":")
        time = int(h) * 60 + int(m)
        end_time = time + int(plan[2])
        new_plans.append([plan[0], time, end_time, int(plan[2])])

    new_plans = sorted(new_plans, key=lambda x: x[1])
    q = deque(new_plans)
    print(q)

    now = new_plans[0][1]
    stop_list = []
    while True:

        name, start, end, time = q.popleft()

        if len(q) == 0:
            answer.append(name)
            break

        # 만약 다음과제보다 빨리 끝난다면, 여유시간이 있다.
        if end < q[0][1]:
            answer.append(name)

            left_time = q[0][1] - end
            # 여유시간동안 stop_list에서 빼서 연산한다.
            while left_time > 0 and stop_list:
                name, start, end, time = stop_list.pop()
                # 여유시간안에 처리가 가능하면
                if left_time - time >= 0:
                    answer.append(name)
                    left_time -= time
                # 처리가 불가하면, 시간만 줄이고 다시 대기열로
                else:
                    stop_list.append([name, start, end, time - left_time])
                    break

        # 같다면, 이어서 다음 과제를 수행한다.
        elif end == q[0][1]:
            answer.append(name)

        # 현재 과제가 다음 과제 시작시간안에 안끝나면, 남은 시간을 줄이고 대기열로 보낸다.
        elif end > q[0][1]:
            stop_list.append([name, start, end, end - q[0][1]])

    # 대기열이 남았다면, 역순으로 붙혀준다.
    if len(stop_list) > 0:
        for i in stop_list[::-1]:
            answer.append(i[0])

    return answer
solution([["a","09:00","30"],["b","09:10","20"],["c","09:15","20"],["d","09:55","10"],["e","10:50","5"]])