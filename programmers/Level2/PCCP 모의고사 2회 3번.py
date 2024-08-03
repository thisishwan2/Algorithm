from collections import deque


def solution(menu, order, k):
    answer = 1
    ordering = deque(order)
    waiting = deque()
    waiting.append(ordering.popleft())

    time = 0
    cur = 0
    extra_cook_time = menu[waiting[0]]
    while ordering and waiting:
        time += k

        while extra_cook_time!=0:
            # 음식조리 완료 시점이 사람 추가 투입 시점보다 같거나 빠르면,
            if cur + extra_cook_time <= time:
                cur += extra_cook_time
                waiting.popleft()  # 음식 조리가 완료된 사람을 뺀다.
                extra_cook_time=0
                if waiting:
                    extra_cook_time = menu[waiting[0]]
            else:
                extra_cook_time = extra_cook_time - (time - cur)
                break
        if ordering:
            waiting.append(ordering.popleft())
            if extra_cook_time == 0:
                extra_cook_time=menu[waiting[0]]
        cur = time

        answer = max(len(waiting), answer)
    # print(answer)
    return answer

solution([5, 12, 30],	[1, 2, 0, 1],	10)
solution([5, 12, 30],	[2, 1, 0, 0, 0, 1, 0]	,10)
solution([5],	[0, 0, 0, 0, 0],	5)


def solution(menu, order, k):
    order_list = []
    current = []

    for i in range(len(order)):
        # 1회 반복에 1회 주문 리스트 추가
        order_list.append(menu[order[i]])

        # 현재의 주문 수 리스트에 추가
        current.append(len(order_list))

        # 제일 앞 손님 음료 제조 시간 차감
        order_list[0] = order_list[0] - k

        # 차감 결과가 음수라면 바로 다음 주문의 제조 시간 차감
        # 음수가 된 주문 리스트에서 제거하여 다음 손님이 제일 앞 손님이 됨
        while order_list and order_list[0] <= 0:
            if len(order_list) >= 2:
                order_list[1] += order_list[0]
            order_list.pop(0)

    # 주문 수 목록에서 제일 큰 수 리턴
    return max(current)