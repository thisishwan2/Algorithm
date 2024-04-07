def make_list(lst, input_str):
    for i in range(len(input_str) - 1):
        # 아스키 코드를 기준으로 A~Z, a~z 안에 포함되는 경우에만 뽑음
        if 65 <= ord(input_str[i]) <= 90 or 97 <= ord(input_str[i]) <= 122:
            if 65 <= ord(input_str[i + 1]) <= 90 or 97 <= ord(input_str[i + 1]) <= 122:
                lst.append(input_str[i].upper() + input_str[i + 1].upper())

    return lst


def jakard(a, b):
    common = 0
    total = 0

    # 공집합의 경우
    if len(a) == 0 and len(b) == 0:
        return 1

    check_common = []
    check_total = []
    for i in a:
        a_i_cnt = a.count(i)
        b_i_cnt = b.count(i)
        # 교집합
        if i not in check_common:
            common += min(a_i_cnt, b_i_cnt)
            check_common.append(i)
        # 합집합
        if i not in check_total:
            total += max(a_i_cnt, b_i_cnt)
            check_total.append(i)

    # b에 대해서도 합집합을 위해 순회를 한번 해줘야함(a에는 포함되지 않은 b의 원소가 존재할 수 있음)
    for i in b:
        a_i_cnt = a.count(i)
        b_i_cnt = b.count(i)
        if i not in check_total:
            total += max(a_i_cnt, b_i_cnt)
            check_total.append(i)

    ans = common / total
    return ans
    # 합집합


def solution(str1, str2):
    answer = 0

    # 다중 집합 원소로 만들기
    A = []
    B = []

    A = make_list(A, str1)
    B = make_list(B, str2)

    answer = jakard(A, B)

    return int(answer * 65536)

# J(A,B)는 두 집합의 교집합 크기/합집합 크기
# 공집합의 경우는 J(A,B) = 1
# 다중 집합(원소 중복 허용)의 경우에는 겹치는 원소에 대해 교집합은 min, 합집합은 max