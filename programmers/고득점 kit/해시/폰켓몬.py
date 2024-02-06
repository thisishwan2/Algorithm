def solution(ls):
    return min(len(ls)/2, len(set(ls)))

# 내 풀이
def solution(nums):
    n = len(nums) // 2  # 최대 가져갈 수 있는 포켓몬 수

    ans = []

    for i in nums:
        if len(ans) == n:
            break
        if i in ans:
            pass
        else:
            ans.append(i)

    answer = len(ans)
    return answer