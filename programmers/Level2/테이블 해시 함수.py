def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    # print(data)

    lst = []
    s_num = 1
    for i in data:
        num = 0
        for j in i:
            num += j % s_num

        lst.append(num)
        s_num += 1
    # print(lst)

    lst = lst[row_begin - 1: row_end]

    num = lst[0]
    for i in range(1, len(lst)):
        num = num ^ lst[i]
    answer = num
    return answer