def solution(s):
    ans = 1e9

    if len(s) == 1:
        return 1

    # 절반만 확인하면 됨
    for split_cnt in range(1, (len(s) // 2) + 1):
        tmp = []
        for i in range(0, len(s), split_cnt):
            tmp.append(s[i:i + split_cnt])

        # print(tmp)

        answer = []
        cnt = 1
        for i in range(len(tmp) - 1):
            if tmp[i] == tmp[i + 1]:
                cnt += 1
            else:
                if cnt != 1:
                    n_tmp = str(cnt) + tmp[i]
                    answer.append(n_tmp)
                    cnt = 1
                else:
                    answer.append(tmp[i])

        # 마지막도 처리해줘야함
        if cnt != 1:
            n_tmp = str(cnt) + tmp[i]
            answer.append(n_tmp)
        else:
            answer.append(tmp[-1])

        # 리스트를 합친다.
        result = "".join(answer)
        ans = min(ans, len(result))
        # print("============")
    return ans