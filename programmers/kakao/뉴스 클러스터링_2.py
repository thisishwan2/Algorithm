import math


def solution(str1, str2):
    # 다중집합 원소로 만든다.
    # 딕셔너리로 관리하자
    dict_1 = {}
    for i in range(len(str1) - 1):
        string = str1[i] + str1[i + 1]
        if string.isalpha():
            upper = string.upper()
            if dict_1.get(upper) == None:
                dict_1[upper] = 1
            else:
                dict_1[upper] += 1

    dict_2 = {}
    for i in range(len(str2) - 1):
        string = str2[i] + str2[i + 1]
        if string.isalpha():
            upper = string.upper()
            if dict_2.get(upper) == None:
                dict_2[upper] = 1
            else:
                dict_2[upper] += 1

    # 교집합 개수
    k = 0
    # 합집합 개수
    h = 0

    # 교집합 구하기
    for key in dict_1.keys():
        if dict_2.get(key) != None:
            k += min(dict_1[key], dict_2[key])

    # 합집합 구하기
    for key in list(dict_1.keys()):
        if dict_2.get(key) != None:
            h += max(dict_1[key], dict_2[key])
            del dict_1[key]
            del dict_2[key]
        else:
            h += dict_1[key]
    for key in dict_2.keys():
        h += dict_2[key]

    if k == 0 and h == 0:
        return 1 * 65536
    else:
        return math.trunc((k / h) * 65536)

