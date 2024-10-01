def solution(files):
    lst = []

    for i, file in enumerate(files):
        tmp = []
        head_flag = True
        head_end_idx = 0
        number_flag = True
        for idx in range(len(file)):
            if head_flag and not file[idx].isdigit() and file[idx + 1].isdigit():
                head_flag = False
                tmp.append(file[:idx + 1])
                head_end_idx = idx
                continue

            # tail이 없는 경우
            if number_flag and idx == len(file) - 1:
                tmp.append(file[head_end_idx + 1:])  # number 담기
                tmp.append("")
                break

            # tail이 있는 경우
            if number_flag and file[idx].isdigit() and not file[idx + 1].isdigit():
                number_flag = False
                tmp.append(file[head_end_idx + 1:idx + 1])  # number 담기
                if idx + 1 < len(file):
                    tmp.append(file[idx + 1:])  # tail 담기
                break
        # 대소문자 구분없애고, number도 int로 바꾼 원소를 추가롤 담는다.
        tmp += [tmp[0].lower(), int(tmp[1]), i]

        lst.append(tmp)
    # print(lst)

    # 정렬
    ans = sorted(lst, key=lambda x: (x[3], x[4], x[5]))  # 대소문자 구분없이 정렬, 숫자로 정렬

    answer = []
    # join
    for i in ans:
        answer.append("".join(i[0:3]))

    return answer