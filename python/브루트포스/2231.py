#내가 풀은코드
#분해법에 대해서는 완벽히 이해했다. 하지만 코드 자체가 매끄럽지 못하다고 생각함.
import sys

n=int(sys.stdin.readline())
#생성자 출력
sum=0
lst=[]
for i in range(n):
    selfnum=i
    sum=i
    #자리수만 더해주기
    while i!=0:
        sum=sum+i%10 #뒷자리 남기기
        i=i//10 # 뒷자리 없애기
    if sum==n:
        lst.append(selfnum)
        print(selfnum)
        break

if len(lst)==0:
    print(0)


#다른 풀이(신기하게도 간결하지만 위의 내 풀이보다 시간이 더 걸렸다. 아마 list(map 하는 부분에서 시간이 더 걸리지 않았나 싶다.))
n=int(input())

res=0

for i in range(1,n+1):
    a=list(map(int, str(i))) # 이부분이 핵심이다. i를 문자로 바꾸고, int 형으로 리스트 화 하는 문법이다.
    res = i+sum(a)
    if res==n:
        print(i)
        break
    if i==n:
        print(0)