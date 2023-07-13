#20055

import sys
input=sys.stdin.readline

n,k = map(int, input().split()) # n은 컨베이어 벨트 길이, k를 넘는 내구도 0칸이 있으면 종료
line=list(map(int, input().split())) #line의 -1번째는 다음에 0번째로 이동
robot=[0]*(n)

cnt=0
res=0
while cnt<k:
    cnt=0
    res+=1

    # 1번
    temp=line[-1]
    temp_ro = robot[-1]
    
    #컨베이어 이동
    for i in range(2*n-2, -1, -1):
        line[i+1]=line[i]
    line[0]=temp

    #로봇이동
    for i in range(n-2, -1, -1):
        robot[i+1]=robot[i]
    robot[0]=temp_ro

    #1번은 list.pop과 insert(0,?)을 사용하면 쉽게 구현 가능

    # 컨베이어 벨트 이동후 도착지점에 로봇이 있으면 내린다.
    if robot[n-1]==1:
        robot[n-1]=0
    
    # 2번
    for i in range(n-2, -1, -1):
        if robot[i+1]==0 and line[i+1]>=1 and robot[i]==1: #현재칸에 로봇이 있고, 다음칸에는 없고, 다음칸 내구도가 1이상일때
            robot[i+1]=robot[i] #로봇이동
            robot[i]=0

            line[i+1]=line[i+1]-1 #다음칸 내구성 -1
            
            if i+1==n-1 and robot[i+1]==1: #만약 이동후 마지막 칸에 로봇이 존재하면
                robot[i+1]=0 #로봇을 내린다.
            
    
    # 3번
    if line[0]>=1:
        robot[0]=1
        line[0]=line[0]-1

    # 4번
    for i in line:
        if i==0:
            cnt+=1
    
print(res)


