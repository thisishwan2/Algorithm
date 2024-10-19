def solution(gems):
    n = len(gems)
    answer = [0, n]
    size = len(set(gems))
    left, right = 0, 0
    gem_dict = {gems[0]: 1}

    while left < len(gems) and right < len(gems):
        if len(gem_dict) == size:  # 모든 보석을 가지면
            if right - left < answer[1] - answer[0]:
                answer = [left + 1, right + 1]
            else:
                gem_dict[gems[left]] -= 1
                if gem_dict[gems[left]] == 0:
                    del gem_dict[gems[left]]
                left += 1
        else:
            right += 1

            if right == n:
                break

            if gem_dict.get(gems[right]) == None:
                gem_dict[gems[right]] = 1
            else:
                gem_dict[gems[right]] += 1

    return answer
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	)