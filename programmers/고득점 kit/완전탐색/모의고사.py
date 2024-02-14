# 내 풀이
def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    one_ans = 0
    two_ans = 0
    three_ans = 0

    for i in range(len(answers)):
        if answers[i] == one[i]:
            one_ans += 1
        if answers[i] == two[i]:
            two_ans += 1
        if answers[i] == three[i]:
            three_ans += 1

    maximum = max(one_ans, two_ans, three_ans)

    if one_ans == maximum:
        answer.append(1)
    if two_ans == maximum:
        answer.append(2)
    if three_ans == maximum:
        answer.append(3)

    return sorted(answer)

# 순환주기를 각각 계산해준 풀이(메모리 효율이 더 좋음)
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

