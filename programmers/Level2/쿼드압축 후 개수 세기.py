def dfs(arr):
    global answer

    # 현재 부분이 모든 같은 값인지 확인
    flag = True
    standard = arr[0][0]
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != standard:
                flag = False
                break
        if flag == False:
            break
    # 모두 같은 값이면
    if flag:
        answer[arr[0][0]] += 1
        return
    else:
        if n == 1:
            return
        else:
            # 4조각으로 쪼갠다.
            mid = n // 2
            for j in range(0, n, mid):
                tmp = []
                for i in range(0, mid):
                    tmp.append(arr[i][j:j + mid])
                dfs(tmp)
                tmp = []
                for i in range(mid, n):
                    tmp.append(arr[i][j:j + mid])
                dfs(tmp)


answer = {}
answer[1] = 0
answer[0] = 0


def solution(arr):
    dfs(arr)
    ans = [answer[0], answer[1]]
    return ans

# solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])