#11286

import sys
import heapq

n=int(sys.stdin.readline())

h=[]

for i in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        if h:
            #인덱스를 가지고 놀려면 아래와 같이(튜플 리스트로 받았을때만 인덱스 가능)
            print(heapq.heappop(h)[1])
        else:
            print(0)
    else:
        #튜플형태로도 전달 가능. 리스트도 가능
        heapq.heappush(h,[abs(a),a])

# 양수 음수를 구분한 풀이
import sys
import heapq

n=int(sys.stdin.readline())
q1=[]#양수
q2=[]#음수

for i in range(n):
    a=int(sys.stdin.readline())

    if a>0:
        heapq.heappush(q1, a)
    elif a<0:
        heapq.heappush(q2, -a)
    
    else:
        if q1 and q2:
            if q1[0]==q2[0]:
                print(-heapq.heappop(q2))
            elif q1[0]>abs(q2[0]):
                print(-heapq.heappop(q2))
            else:
                print(heapq.heappop(q1))
        elif q1:
            print(heapq.heappop(q1))
        elif q2:
            print(-heapq.heappop(q2))
        else:
            print(0)