def solution(numbers, hand):
    answer = ''

    number = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2],
              0: [3, 1], "*": [3, 0], "#": [3, 2]}

    now_left = "*"
    now_right = "#"
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            now_left = i
        elif i in [3, 6, 9]:
            answer += "R"
            now_right = i

        else:
            left_move = abs(number[now_left][0] - number[i][0]) + abs(number[now_left][1] - number[i][1])
            right_move = abs(number[now_right][0] - number[i][0]) + abs(number[now_right][1] - number[i][1])

            if left_move < right_move:
                answer += "L"
                now_left = i
            elif left_move > right_move:
                answer += "R"
                now_right = i
            else:
                if hand == "right":
                    answer += "R"
                    now_right = i
                else:
                    answer += "L"
                    now_left = i

    return answer