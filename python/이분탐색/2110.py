# 문제의 핵심은 집들이 수직선 상에 있다는 말이다.
# 즉, 1,2,4,8,9 이렇게 있는게 아니고, 
# |1|,|2|,3,|4|,5,6,7,|8|,|9| 와 같이 모든 점이 있고, 그 위에 집이 있는것이다.
# 따라서 이분탐색을 진행하기 위해, 주어진 집들중 중간값(4)이 mid기 되는게 아닌,
# 집들 사이의 최소거리와 최대거리의 중앙값이 mid가 된다.(사이거리로 하는 이유는 우리가 구하고자 하는 값은 간격이기 때문)
# 집들 사이의 최소거리 (집이 1,2 와 같이 바로 다음에 있는경우) : 1 
# 집들 사이의 최대거리 (1,2,4,8,9 일때 9-1인 값): 8
# 따라서 mid = 1+8//2

# 이제 이 mid를 가지고, 1번 집과의 거리가 mid 이상인 수를 count한다.
# count가 설치할 공유기 갯수를 만족하지 못하면, mid 값을 줄인다.

import sys
input=sys.stdin.readline

n,c = map(int,input().split())

h=[]
for _ in range(n):
    h.append(int(input()))
h.sort()

result=0

def bs(start,end):
    while start<=end:
        mid=(start+end)//2

        cnt=1 #h[0]에 이미 설치를 했다고 가정.
        ts=h[0] #시작
        for i in range(n):
            if h[i] - ts >=mid:
                cnt+=1
                ts=h[i]
        if cnt>=c:
            result=mid
            start=mid+1
        else:
            end=mid-1
    return result

if c==2:
    print(h[n-1]-n[0])
else:
    print(bs(1,h[n-1]-h[0]))
    #최소, 최대거리 (최소거리가 1이 아닐수도있는데 1로 잡는것은 그냥 러프하게 1부터 잡는것.)



"""

import math,sys
input = sys.stdin.readline

n,c = map(int,input().split())
h = [int(input()) for i in range(n)]
h.sort()
start,end = 1, h[n-1] - h[0]
# 집 사이의 최소 거리, 최대 거리
result = 0

if c == 2:
    print(h[n-1] - h[0])
    # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
else:
    while(start < end):
        mid = (start + end)//2

        count = 1
        ts = h[0]
        # 마지막으로 설치된 공유기의 위치
        for i in range(n):
            if h[i] - ts >= mid:
                count+=1
                ts = h[i]
        if count >= c:
            result = mid
            start = mid + 1
        elif count < c:
            end = mid
    print(result)

"""