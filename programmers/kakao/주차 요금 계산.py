# 주차 요금 공식
# 기본요금 + [전체 시간 - 기본 시간/단위시간] * 단위 요금(if 전체시간> 기본시간)
# 초과 시간이 단위시간으로 나누어 떨어지지 않으면 올림

# 기본요금 (단위 요금(if 전체시간<= 기본시간))

# 주차 시간은 00:00~23:59 까지

import math


def solution(fees, records):
    # fees[0] = 기본 시간, fees[1] = 기본 요금, fees[2] = 단위 시간, fees[3] = 단위 요금

    in_dict = {}
    out_dict = {}
    time_dict = {}
    money = {}

    for i in records:
        time, number, in_out = i.split(" ")
        hour, minute = time.split(":")
        total_time = int(hour) * 60 + int(minute)

        if number not in time_dict:
            time_dict[number] = 0

        if in_out == "IN":
            in_dict[number] = total_time
        else:
            out_dict[number] = total_time

        if (number in in_dict) and (number in out_dict):
            time_dict[number] += (out_dict[number] - in_dict[number])
            in_dict.pop(number)
            out_dict.pop(number)

    for i in in_dict.keys():
        time_dict[i] += (23 * 60 + 59) - in_dict[i]

    answer = []
    for i in time_dict.keys():
        if time_dict[i] > fees[0]:  # 기본 요금보다 큰 경우
            ans = fees[1] + math.ceil((time_dict[i] - fees[0]) / fees[2]) * fees[3]
        else:
            ans = fees[1]
        answer.append([i, ans])

    answer = sorted(answer, key=lambda x: x[0])

    res = []
    for i in answer:
        res.append(i[1])

    return res