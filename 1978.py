n = int(input())

m=list(map(int,input().split()))

cnt=0
#a=0 이부분을 잘못했었다. 이렇게 a를 전역변수 취급하면 한번 a=1이 된후로 전역변수이므로 계속 a=1이 유지된다.
for i in m:
    a=0 #이렇게 수정하면 된다.
    if i==1:    #1은 소수가 아니므로 패스한다
        pass
    else:
        for j in range(2,i):    #2는 for문이 작동하지 않는다.
            if i%j==0:  #나눠지는 몫이 있으면
                a=1
        if a==0:    #없으면
            cnt+=1
print(cnt)
