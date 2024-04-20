# 동점은 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단합니다.
def solution(survey, choices):
    # sheet = [[["R",0],["T",0]], [["C",0], ["F",0]], [["J",0], ["M",0]],[["A",0],["N",0]]]
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i, val in enumerate(survey):
        ["AN", "CF", "MJ", "RT", "NA"]
        [5, 3, 2, 7, 5]
        disagree = val[0]
        agree = val[1]

        if choices[i] <= 3:
            if choices[i] == 1:
                tmp = 3
            elif choices[i] == 3:
                tmp = 1
            else:
                tmp = choices[i]

            dic[disagree] += tmp

        elif choices[i] >= 5:
            tmp = choices[i] - 4
            dic[agree] += tmp
        # print(dic)
    tmp = []
    answer = ''

    for i in dic.keys():
        cnt = dic[i]
        tmp.append([i, cnt])

        if len(tmp) == 2:
            if tmp[0][1] > tmp[1][1]:
                answer += tmp[0][0]
            elif tmp[0][1] < tmp[1][1]:
                answer += tmp[1][0]
            else:
                if tmp[0][0] > tmp[1][0]:
                    answer += tmp[1][0]
                else:
                    answer += tmp[0][0]
            tmp = []
    return answer