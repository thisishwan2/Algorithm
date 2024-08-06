import heapq


def solution(operations):
    max_hq = []
    min_hq = []

    for i in operations:
        cmd, num = i.split()
        if cmd == "I":
            heapq.heappush(max_hq, -int(num))
            heapq.heappush(min_hq, int(num))

        else:
            if num == "1" and len(max_hq) > 0:
                n = heapq.heappop(max_hq)
                min_hq.remove(-n)

            elif num == "-1" and len(min_hq) > 0:
                n = heapq.heappop(min_hq)
                max_hq.remove(-n)

    if len(max_hq) == 0:
        return [0, 0]
    else:
        return [max(min_hq), min(min_hq)]
