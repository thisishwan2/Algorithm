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



''' 과거 풀이'''

def solution(info, query):
    answer = []

    language = {}
    position = {}
    career = {}
    soul_food = {}
    score = {}
    for idx, val in enumerate(info):
        tmp = val.split()

        # 언어 등록
        if language.get(tmp[0]) == None:  # 처음 등록
            language[tmp[0]] = [idx]
        else:
            language[tmp[0]].append(idx)

        # 포지션 등록
        if position.get(tmp[1]) == None:  # 처음 등록
            position[tmp[1]] = [idx]
        else:
            position[tmp[1]].append(idx)

        # 경력 등록
        if career.get(tmp[2]) == None:  # 처음 등록
            career[tmp[2]] = [idx]
        else:
            career[tmp[2]].append(idx)

        # 소울 푸드 등록
        if soul_food.get(tmp[3]) == None:  # 처음 등록
            soul_food[tmp[3]] = [idx]
        else:
            soul_food[tmp[3]].append(idx)

        # 코테 점수 등록
        score[idx] = tmp[4]

    n = len(info)  # 지원자 수

    for i in query:
        condition = i.split()
        # 모두를 후보로 등록한다.
        candidate = {}
        for num in range(n):
            candidate[num] = ""

        for j in range(8):
            if j == 0:  # 언어
                if condition[j] == "-":
                    continue
                else:
                    for k in list(candidate.keys()):
                        if k not in language[condition[j]]:
                            del candidate[k]


            elif j == 2:  # 직무
                if condition[j] == "-":
                    continue
                else:
                    for k in list(candidate.keys()):
                        if k not in position[condition[j]]:
                            del candidate[k]


            elif j == 4:  # 경력
                if condition[j] == "-":
                    continue
                else:
                    for k in list(candidate.keys()):
                        if k not in career[condition[j]]:
                            del candidate[k]

            elif j == 6:  # 소울 푸드
                if condition[j] == "-":
                    continue
                else:
                    for k in list(candidate.keys()):
                        if k not in soul_food[condition[j]]:
                            del candidate[k]

            elif j == 7:  # 코테 점수
                if condition[j] == "-":
                    continue
                else:
                    for k in list(candidate.keys()):
                        if int(score[k]) < int(condition[j]):
                            del candidate[k]

        answer.append(len(candidate))

    return answer


# 정확성 통과, 효율성 실패
def solution(info, query):
    answer = []

    language = {}
    position = {}
    career = {}
    soul_food = {}
    score = {}
    for idx, val in enumerate(info):
        tmp = val.split()

        # 언어 등록
        if language.get(tmp[0]) == None:  # 처음 등록
            language[tmp[0]] = [idx]
        else:
            language[tmp[0]].append(idx)

        # 포지션 등록
        if position.get(tmp[1]) == None:  # 처음 등록
            position[tmp[1]] = [idx]
        else:
            position[tmp[1]].append(idx)

        # 경력 등록
        if career.get(tmp[2]) == None:  # 처음 등록
            career[tmp[2]] = [idx]
        else:
            career[tmp[2]].append(idx)

        # 소울 푸드 등록
        if soul_food.get(tmp[3]) == None:  # 처음 등록
            soul_food[tmp[3]] = [idx]
        else:
            soul_food[tmp[3]].append(idx)

        # 코테 점수 등록
        score[idx] = tmp[4]
    # print(language)
    # print(position)
    # print(career)
    # print(soul_food)
    # print(score)

    n = len(info)  # 지원자 수

    for i in query:
        candidate = [0] * n  # 인덱스: 후보 번호, 값: 조건에 True가 되는 횟수 즉, 5번다 만족하면 그 인원은 합격할 수 있는 지원자
        condition = i.split()

        for j in range(8):
            if j == 0:  # 언어
                if condition[j] == "-":
                    for k in range(n):
                        candidate[k] += 1
                else:
                    for k in language[condition[j]]:
                        candidate[k] += 1

            elif j == 2:  # 직무
                if condition[j] == "-":
                    for k in range(n):
                        candidate[k] += 1
                else:
                    for k in position[condition[j]]:
                        candidate[k] += 1


            elif j == 4:  # 경력
                if condition[j] == "-":
                    for k in range(n):
                        candidate[k] += 1
                else:
                    for k in career[condition[j]]:
                        candidate[k] += 1


            elif j == 6:  # 소울 푸드
                if condition[j] == "-":
                    for k in range(n):
                        candidate[k] += 1
                else:
                    for k in soul_food[condition[j]]:
                        candidate[k] += 1


            elif j == 7:  # 코테 점수
                if condition[j] == "-":
                    for k in range(n):
                        candidate[k] += 1
                else:
                    for k in score.keys():
                        if int(score[k]) >= int(condition[j]):
                            candidate[k] += 1
        # print(candidate)

        cnt = 0
        for i in candidate:
            if i == 5:
                cnt += 1
        answer.append(cnt)
    return answer

