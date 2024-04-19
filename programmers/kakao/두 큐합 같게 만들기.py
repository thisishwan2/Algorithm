from collections import deque


def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    if total % 2 == 0:
        queue_total = total // 2
    else:
        return -1

    count = 0
    n = len(queue1)

    # 합을 미리 구함
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # 큐 생성
    q1 = deque()
    q2 = deque()

    for i in queue1:
        q1.append(i)

    for i in queue2:
        q2.append(i)

    # 탈출 조건이 필요
    turn = 0
    while turn < 3 * n:

        turn += 1
        if sum2 == queue_total:
            return count

        elif sum2 > queue_total:
            tmp = q2.popleft()  # 큐를 이용해서 popleft 하지 않고 그냥 리스트의 pop(0)을 쓰면 결국 o(n)이 걸림
            sum2 -= tmp
            q1.append(tmp)
            sum1 += tmp
            count += 1

        elif sum2 < queue_total:
            tmp = q1.popleft()
            sum1 -= tmp
            q2.append(tmp)
            sum2 += tmp
            count += 1

    answer = -1
    return answer