import sys
input=sys.stdin.readline

def matrix(arry, b):
    if b==1:
        return arry
    else:
        temp=matrix(arry, b//2)
        if b%2==0:
            return cal(temp, temp)
        else:
            return cal(cal(temp, temp), arry)


def cal(arry1, arry2):
    result=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += arry1[i][k]*arry2[k][j]
            result[i][j]%=1000
    return result


n,b = map(int,input().split())

arry=[]

for i in range(n):
    lst=list(map(int, input().split()))
    arry.append(lst)


ans = matrix(arry, b)

for row in ans:
    for col in row:
        print(col % 1000, end=" ") # 1번만 제곱하는 경우는 기존 arry  그대로 리턴되므로 [[1000, 1000], [1000, 1000]] 과 같은 경우 %1000을 하지 않으면 행렬 그대로 출력된다. 이경우는 1000보다 작은 조건 불충족
    print()