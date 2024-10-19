def dfs(order, cnt, tmp, start):
    if len(tmp) == cnt:
        if dict.get(tmp) == None:
            dict[tmp] = 1
        else:
            dict[tmp] += 1
        return
    for i in range(start, len(order)):
        dfs(order, cnt, tmp + order[i], i + 1)


def solution(orders, course):
    global dict
    answer = []
    for cnt in course:
        dict = {}
        for o in orders:
            o = sorted(o)
            dfs(o, cnt, "", 0)

        ans = []
        maxi = 0
        for key in dict.keys():
            if dict[key]<2:
                continue
            if maxi<dict[key]:
                maxi=dict[key]
                ans=[key]
            elif maxi==dict[key]:
                ans.append(key)

        answer.extend(ans)
    return sorted(answer)
# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]		)