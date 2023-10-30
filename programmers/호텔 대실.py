# 한번 사용한 객실은 퇴실 시간 기준 10분간 청소 후 손님 받음
# 필요한 최소 객실수를 return

# 본 문제의 핵심은 각 방별 중 마지막 시간 제일 작은 놈 + 10분 이랑 그 다음에 올 것을 비교해야됨

def solution(book_time):
    lst = []

    # 문자열 시간 -> 정수형 시간
    for i in book_time:
        start_x, start_y = i[0].split(":")
        end_x, end_y = i[1].split(":")

        start = int(start_x) * 60 + int(start_y)
        end = int(end_x) * 60 + int(end_y)

        lst.append([start, end])

    print(lst)

    # 예약 시작 시간 기준 정렬
    book_time = sorted(lst)
    print(book_time)

    ## 위는 맞음
    room = 0
    end_time = [10000] * 1000
    end_time[0] = book_time[0][1]

    for i in range(1, len(book_time)):
        start = book_time[i][0]
        end = book_time[i][1]

        # 마지막 종료 시간 + 10 분 보다 다음 시작시간이 크면 방을 늘리지 않아도 됨
        if min(end_time) + 10 <= start:
            idx = end_time.index(min(end_time))
            end_time[idx] = end  # 마지막 종료 시간의 인덱스를 구해서 end_time 배열에서 해당 room의 마지막 시간을 업데이트
            continue
        else:
            room += 1
            end_time[room] = end

    return room + 1