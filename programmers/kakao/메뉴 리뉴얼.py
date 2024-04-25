# 조합
def com(order, course, answer):
    def generate(string):

        if len(string) == course:
            if string not in answer.keys():
                answer[string] = 1
            else:
                answer[string] += 1
            return

        # 조합이므로 무조건 다음 녀석을 뽑을건데, 없는 경우에는 0을 설정
        start = order.index(string[-1]) + 1 if string else 0
        for i in range(start, len(order)):
            string+=(order[i])
            generate(string)
            string = string[:-1]

    generate("")


def solution(orders, course):
    order_candidate = {}
    # 최소 2번이상 주문됐는지 확인
    for i in orders:
        order = list(i)
        for j in order:
            if j not in order_candidate:
                order_candidate[j] = 1
            else:
                order_candidate[j] += 1

    candidate = []
    for i in order_candidate.keys():
        if order_candidate[i] >= 2:
            candidate.append(i)

    # print(candidate)

    answer = {}
    # 가장 많이 주문한 조합을 찾는다.
    for i in orders:
        order = sorted(list(i))

        for j in order:
            if j not in candidate:
                order.remove(j)

        # order에 대해 course에 가능한 경우를 만들고 딕셔너리에 넣는다.
        for i in course:
            com(order, i, answer)
    print(answer)

    ans={}
    res = []
    for i in course:
        ans[i] = []
        cnt = 0
        for j in answer.keys():
            if len(j) == i:
                cnt = max(cnt, answer[j])

        for j in answer.keys():
            if len(j) == i and answer[j]>=2 and answer[j] == cnt:
                res.append(j)
    res = sorted(res)
    print(res)
    return res

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	, [2,3,4])