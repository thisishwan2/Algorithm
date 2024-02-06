import math
from collections import deque
def solution(progresses, speeds):
    tmp = []

    for i, j in zip(progresses, speeds):
        tmp.append(math.ceil((100 - i) / j))
    print(tmp)

    answer = []
    q = deque()
    for i in tmp:
        q.append(i)

    print(q)

    cnt = 0
    temp = tmp[0]

    tmp.append(200)
    for i in tmp:
        if (i - temp) <= 0:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            temp = i

    return answer

'''
정석 풀이
'''

# 1. -((p-100)//s) 이 부분은 2.333 과 같은 숫자를 올림해야되는데, 그럴때 math 모듈 사용 없이도 올림하기 위해서 일부러 -2.33을 만들고 몫으로 나눠줌으로써 -3 을 만드는 방식임
# 2. for문의 첫번째랑, q의 가장 마지막에 있는 걸리는 날짜보다 큰 값인 경우에 append함 (q에는 [배포까지 걸리는 날짜, 1] 이 들어감)
# 3. 그 외에는 가장 최근에 넣은 q에 +1 해주는 방식
# 4. 이렇게 하면 5,10,1,1,20,1 과 같이 걸리는 날짜가 있을때, 이전값보다 커지는 값일때 새로운 1을 추가할 수 있음(배포하는 개수를 말함)

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]