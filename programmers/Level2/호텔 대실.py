# def solution(book_time):
#     minute = []
#     for s,e in book_time:
#         tmp = []
#         h,m = s.split(":")
#         tmp.append(int(h)*60+int(m))
#         h,m = e.split(":")
#         if int(h)*60+int(m)+10>1440:
#             tmp.append(1440)
#         else:
#             tmp.append(int(h)*60+int(m)+10)
#         minute.append(tmp)

#     minute = sorted(minute)
#     print(minute)

#     dp = [0]*(60*24)
#     for s,e in minute:
#         for m in range(s,e):
#             dp[m]+=1
#     return max(dp)


import heapq


def solution(book_time):
    minute = []
    for s, e in book_time:
        tmp = []
        h, m = s.split(":")
        tmp.append(int(h) * 60 + int(m))
        h, m = e.split(":")
        if int(h) * 60 + int(m) + 10 > 1440:
            tmp.append(1440)
        else:
            tmp.append(int(h) * 60 + int(m) + 10)
        minute.append(tmp)

    minute = sorted(minute)
    answer = 0
    heap = []

    for s, e in minute:

        # 방이 있고, 이번 타임의 시작시간이 힙의 가장 빠른 종료시간보다 크면 그 방 이용
        if heap and s >= heap[0]:
            heapq.heappop(heap)
        # 힙이 비거나, 종료시간보다 빨리 시작한다면
        else:
            answer += 1

        heapq.heappush(heap, e)
    return answer


