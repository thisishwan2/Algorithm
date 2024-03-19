import sys
input=sys.stdin.readline

n,l = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# print(arr)

def rotate(arr):
    new_arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nx=j
            ny=n-i-1
            new_arr[nx][ny]=arr[i][j]
    return new_arr

def check(arr):
    bridge = [0 for _ in range(n)]
    for i in range(1, n):
        if abs(arr[i]-arr[i-1])>=2:
            return False

        # 현재가 이전보다 작음 (3 -> 2) => 오른쪽으로 스캔
        if arr[i]<arr[i-1]:
            for j in range(l):
                if i+j >=n or bridge[i+j]==1 or arr[i+j]!=arr[i]: # 배열범위를 벗어난 경우 or 이미 경사로를 설치한 경우 or 높이가 다른 경우
                    return False
                if arr[i]==arr[i+j]:
                    bridge[i+j]=1

        # 현재가 이전보다 큼 (2->3) => 왼쪽 스캔
        elif arr[i]>arr[i-1]:
            for j in range(l):
                if i-j-1<0 or bridge[i-j-1]==1 or arr[i-1]!=arr[i-j-1]: # -1을 전체적으로 해야함 왜냐면 나는 지금 3의 위치이므로 2부터 탐색해야돼서
                    return False
                if arr[i-1]==arr[i-j-1]:
                    bridge[i-j-1]=1

    return True

cnt=0
for i in range(n):
    res = check(arr[i])
    if res == True:
        cnt+=1

arr = rotate(arr)
for i in range(n):
    res = check(arr[i])
    if res == True:
        cnt+=1
print(cnt)

