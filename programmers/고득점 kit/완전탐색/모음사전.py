def dfs(tmp, word_alpha):
    if 1 <= len(tmp) < 5:
        words.append("".join(tmp))
    elif len(tmp) == 5:
        words.append("".join(tmp))
        return

    for i in range(len(word_alpha)):
        tmp.append(word_alpha[i])
        dfs(tmp, word_alpha)
        tmp.pop()


words = []


def solution(word):
    word_alpha = ['A', 'E', 'I', 'O', 'U']

    # 모든 경우를 다 구해서 sort 때린다.
    dfs([], word_alpha)
    answer = words.index(word) + 1
    return answer

solution('AAAAE')