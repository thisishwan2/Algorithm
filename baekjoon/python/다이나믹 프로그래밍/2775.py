#꼭 다시보기!!!
#2차원 배열로도 풀어볼 수 있을거같은데..
#재귀로도 가능하지만 시간 초과가 된다.
t=int(input())


for _ in range(t):
    k=int(input())  #층
    n=int(input())  #호수
    #people 0층 각 호의 사람들 수를 리스트로
    people = [i for i in range(1,n+1)]
    
    #0층을 제외하고 1층부터 k층까지의 반복
    for x in range(k):
        #1호는 1로 고정이니 인덱스상 0을 제외한 1부터 n-1까지(n은 아래식으로 도출)
        for y in range(1,n):
            #ex)1층 2호는 0층 2호 + 0층 1호 = people 1+ people0= 2+1 와 같은 방식으로 people의 인덱스를 1부터 계속 변경
            people[y]=people[y]+people[y-1]

    print(people[-1])









#2차원 배열을 생성하고 맞는 값을 넣어주기

t=int(input())


for i in range(t):
    k=int(input())
    n=int(input())
    #배열생성
    arr=[[0 for col in range(n)] for row in range(k+1)] #행(row)는 0층이 있으니 +1 해준다.

    for a in range(1,n+1):  #0층을 배열에 표현
        arr[0][a-1]=a

    for floor in range(1,k+1):  #1층부터 k층까지
        for room in range(n):
            if room == 0:
                arr[floor][room]=1  #0번째 인덱스 즉, 1호실에는 무조건 1명만 있다.
            else:
                arr[floor][room]=arr[floor-1][room]+arr[floor][room-1]  #지정한 층의 왼쪽방과 지정한 층의 아래방을 더하면 지정한 층의 사람수가 나온다.
    print(arr[k][n-1])  #n-1은 인덱스로 접근이기때문

    #참고 https://yuuj.tistory.com/4
