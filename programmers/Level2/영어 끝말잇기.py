def solution(n, words):
    answer = []

    duplicate = [words[0]]
    prev = words[0]

    for i in range(1, len(words)):

        # 끝말이 안맞으면
        if words[i][0] != prev[-1]:
            return [i % n + 1, i // n + 1]

        else:
            if words[i] in duplicate:
                return [i % n + 1, i // n + 1]

            else:
                prev = words[i]
                duplicate.append(words[i])

    return [0, 0]
solution(3,	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])