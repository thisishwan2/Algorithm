def solution(files):
    head_dict = []
    number_dict = []
    tail_dict = []

    for i, v in enumerate(files):

        tail_flag = False
        number_finish_flag = False

        head = ""
        number = ""
        tail = ""

        for idx, val in enumerate(v):
            if val.isnumeric() == False and tail_flag == False:  # 문자열
                head += val
            elif val.isnumeric() == False and tail_flag == True:
                number_finish_flag = True  # 이걸 true로 두는 이유는 tail에서도 숫자가 나올 수 있기 때문
                tail += val
            elif val.isnumeric():  # 숫자면
                if number_finish_flag == False:
                    number += val
                    tail_flag = True
                else:
                    tail += val

        head_dict.append([i, head.upper(), head])
        number_dict.append([i, int(number), number])
        tail_dict.append([i, tail])

    # print(head_dict)
    # print(number_dict)
    # print(tail_dict)

    res = []
    for i in range(len(head_dict)):
        res.append(head_dict[i] + number_dict[i] + tail_dict[i])
    # print(res)

    result = sorted(res, key=lambda x: (x[1], x[4], x[6]))
    # print(result)

    answer = []
    for i in result:
        head = i[2]
        number = i[5]
        tail = i[7]
        file_name = head + number + tail
        answer.append(file_name)

    return answer

# solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])