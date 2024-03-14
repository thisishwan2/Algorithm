def solution(s):

    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    if s.isdigit():
        return int(s) # 바로리턴

    # 숫자면 넘어가고 문자열이라면 다음 숫자가 나올때까지 단어를 완성한다.
    # 문자열이 이어져있을수도 있으므로 한단어씩 문자열에 합칠때마다 eng배열에 존재하는지 확인하고 있으면 temp를 빈문자열로 초기화시킨다.

    answer = ''
    temp = ''
    for i in s:
        if i.isdigit():
            answer+=i
        # 문자열이면
        else:
            temp += i
            if temp in eng:
                answer += str(eng.index(temp))
                temp = ''

    #print(answer)
    return int(answer)


def solution(s):
    answer = ""
    dictionary = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                  "eight": "8", "nine": "9"}

    for eng, num in dictionary.items():
        if eng in s:
            s = s.replace(eng, num)

    return int(s)