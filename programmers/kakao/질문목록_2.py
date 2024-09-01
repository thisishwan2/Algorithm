def solution(numbers, hand):
    leftx, lefty = 3, 0
    rightx, righty = 3, 2

    phone_dict = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2],
                  0: [3, 1]}

    answer = ""
    for i in numbers:
        if i in (1, 4, 7):
            answer += "L"
            leftx, lefty = phone_dict.get(i)
        elif i in (3, 6, 9):
            answer += "R"
            rightx, righty = phone_dict.get(i)
        else:
            midx, midy = phone_dict.get(i)
            left_d = abs(leftx - midx) + abs(lefty - midy)
            right_d = abs(rightx - midx) + abs(righty - midy)

            if left_d > right_d:
                answer += "R"
                rightx, righty = phone_dict.get(i)

            elif left_d == right_d:
                if hand == "left":
                    answer += "L"
                    leftx, lefty = phone_dict.get(i)
                else:
                    answer += "R"
                    rightx, righty = phone_dict.get(i)
            elif left_d < right_d:
                answer += "L"
                leftx, lefty = phone_dict.get(i)
    return answer

