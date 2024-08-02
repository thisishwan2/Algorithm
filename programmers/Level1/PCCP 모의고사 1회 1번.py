def solution(input_string):
    answer = set()
    for i in range(len(input_string)):
        alpha = input_string[i]
        other_alpha = False
        index = i
        while index < len(input_string) - 1:
            index += 1

            if input_string[index] == alpha and other_alpha == False:
                continue
            elif input_string[index] != alpha:
                other_alpha = True
            elif input_string[index] == alpha and other_alpha == True:
                answer.add(input_string[index])
                break
        if len(answer)==0:
            answer.add("N")
    answer=list(answer)
    answer.sort()
    # print(*answer, sep="")
    return "".join(answer)


# solution("edeaaabbccd")
