# 모든 경우를 미리 만들고, 딕셔너리를 활용하여 알맞는 경우에 대해 이분탐색을 수행한다.
def solution(info, query):
    # 모든 경우의 수를 미리 만들어 놓는다.
    avaliable = {}
    for i in ['cpp', 'java', 'python', '-']:
        for j in ['backend', 'frontend', '-']:
            for k in ['junior', 'senior', '-']:
                for l in ['chicken', 'pizza', '-']:
                    avaliable[(i, j, k, l)] = []

    # print(avaliable)

    # info의 정보에서 가능한 케이스('-'를 고려)를 바탕으로 위에서 만든 케이스에 해당하는 부분에 점수를 넣는다.
    for _ in info:
        tmp = _.split()

        for i in [tmp[0], '-']:
            for j in [tmp[1], '-']:
                for k in [tmp[2], '-']:
                    for l in [tmp[3], '-']:
                        avaliable[(i, j, k, l)].append(int(tmp[4]))

    # print(avaliable)

    # 이진 탐색을 위해 avaliable에서 value인 점수들을 오름차순으로 정렬한다
    for i in avaliable.keys():
        avaliable[i].sort()

    # print(avaliable)
    answer = []
    for q in query:
        q = q.split()

        # 가능한 케이스에 해당하는 점수 리스트를 구한다.
        score = avaliable[q[0], q[2], q[4], q[6]]

        # q[7]보다 큰 점수인 사람의 명수를 구해야하니, 완탐 대신 이진탐색으로 찾는다.
        target = int(q[7])
        start = 0
        end = len(score)

        while start < end:
            mid = (start + end) // 2

            if target > score[mid]:
                start = mid + 1
            elif target <= score[mid]:
                end = mid

        answer.append(len(score) - end)

    return answer