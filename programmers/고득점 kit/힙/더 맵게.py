import heapq

def solution(scoville, K):
    answer = 0

    h = []
    for i in scoville:
        heapq.heappush(h, i)

    while True:
        if len(h) == 1 and h[0] < K:
            return -1
        if h[0] >= K:
            return answer
        else:
            answer += 1
            minimum1 = heapq.heappop(h)
            minimum2 = heapq.heappop(h)

            mix_scoville = minimum1 + (minimum2 * 2)

            heapq.heappush(h, mix_scoville)


