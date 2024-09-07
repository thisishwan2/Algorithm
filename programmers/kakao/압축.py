def solution(msg):
    answer = []

    dict = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
        'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
        'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }

    w = ""
    index = 0
    dict_index = 27
    while index<len(msg):
        last = False
        w = msg[index]
        if index + 1 < len(msg):
            c = msg[index + 1]
            while dict.get(w + c) != None:
                w += c
                index += 1
                if index + 1 < len(msg):
                    c = msg[index + 1]
                else: # 마지막이라면
                    last=True
                    break
        else:
            last = True
        if last:
            answer.append(dict[w])
            break
        else:
            dict[w + c] = dict_index
            answer.append(dict[w])
            dict_index+=1
            index += 1

    return answer
# print(solution("KAKAO"))