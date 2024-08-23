# 처음 접근 방식은 싸우다가 피가 0이하일때, 지금껏 싸운 목록에서 제일 큰 값에 대해 무적권을 사용
# 이때, 싸운 목록에서 제일 큰 값을 리스트로 관리 => 사고를 좀 바꾸면 힙으로 관리 가능
# import heapq
#
#
# def solution(n, k, enemy):
#     answer = 0
#
#     h = []
#     for i in enemy:
#         heapq.heappush(h, -i)
#         if n - i >= 0:
#             n -= i
#         else:
#             if k==0:
#                 break
#             else:
#                 k -= 1
#                 max_ = -heapq.heappop(h)
#                 n += max_
#
#         answer += 1
#     return answer
import heapq


def solution(n, k, enemy):
    answer = 0

    h = []
    for i in enemy:
        heapq.heappush(h, -i)
        if n - i >= 0:
            n -= i
        else:
            if k==0:
                break
            else:
                k -= 1
                max_ = -heapq.heappop(h)
                n += max_-i

        answer += 1
    return answer
solution(7,	3,	[4, 2, 4, 5, 3, 3, 1])