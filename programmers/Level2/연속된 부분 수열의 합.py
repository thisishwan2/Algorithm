# def solution(sequence, k):
#     answer = []
#     start = 0
#     end = 0
#     total = 0

#     while end < len(sequence):
#         total+=sequence[end]

#         # 합이 k보다 큰 경우와 start가 end보다 작을때는 start 부분을 빼서 값을 낮춘다.
#         while total>k and start<=end:
#             total-=sequence[start]
#             start+=1

#         if total == k:
#             answer.append([start,end])

#         end+=1

#     answer = sorted(answer, key=lambda x: (x[1] - x[0], x[0]))
#     # print(answer)
#     return answer[0]

def solution(sequence, k):
    answer = []
    start = 0
    end = 0
    total = 0

    while start != len(sequence) and end <= len(sequence):

        if total<k:
            if end == len(sequence):
                break
            total += sequence[end]
            end+=1

        elif total>k:
            total -= sequence[start]
            start+=1

        elif total==k:
            answer.append([start,end-1])
            total -= sequence[start]
            start+=1


    answer = sorted(answer, key=lambda x: (x[1] - x[0], x[0]))
    # print(answer)
    return answer[0]
