import heapq


def solution(ability, number):
    # n명중 가장 능력치가 낮은 2명을 뽑는 것을 number 번 반복
    # 힙큐를 쓰면 될듯?
    hq = []

    for i in ability:
        heapq.heappush(hq, i)

    for i in range(number):
        num1 = heapq.heappop(hq)
        num2 = heapq.heappop(hq)
        total = num1 + num2
        heapq.heappush(hq, total)
        heapq.heappush(hq, total)

    return sum(hq)