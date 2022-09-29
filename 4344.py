c=int(input())

for i in range(c):
    a=list(map(int, input().split()))
    b=a[0]
    a.remove(a[0])
    avg=sum(a)/b
    cnt=0
    for j in a:
        if j>avg:
            cnt+=1
    result=(cnt/b)*100
    print(f'{result:0.3f}%')        #포매팅 유의

#조금더 깔끔한 풀이
c=int(input())

for i in range(c):
    a=list(map(int, input().split()))
    avg=sum(a[1:])/a[0]
    cnt=0
    for j in a[1:]:
        if j>avg:
            cnt+=1
    result=cnt/a[0] *100
    print(f'{result:0.3f}%')    