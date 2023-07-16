#14499
# 전개도상에서 로테이션이 핵심임
# 예로 
# 아래로 굴리면 맨 아래의 요소가 맨 위로 올라옴. 그렇게 한 열이 밑으로 한칸씩 내려감
# 위로 굴리면 그 반대
# 우로 귤리면 행요소가 오른쪽으로 이동하고, 맨 오른쪽이 맨 밑으로, 맨 밑이 맨 왼쪽으로 이동
# 사실 알고보니 위에 푸는 방식보다 더 쉬운방식이 있다..

# 인덱스 0부터 5까지 각각의 인덱스가 위쪽, 뒤쪽, 오른쪽, 왼쪽, 앞쪽, 바닥 이라고 했을 때
# 북쪽으로 굴린 경우 [1,2,3,4,5,6]=>[5,1,3,4,6,2]
# 남쪽으로 굴린 경우 [1,2,3,4,5,6]=>[2,6,3,4,1,5]
# 동쪽으로 굴린 경우 [1,2,3,4,5,6]=>[4,2,1,6,5,3]
# 서쪽으로 굴린 경우 [1,2,3,4,5,6]=>[3,2,6,1,5,4]
# 위의 규칙만 알면 된다.


import sys
input=sys.stdin.readline

def move(i):
    global x,y

    if i==1:
        if 0<=x<n and 0<=y+1<m:
            temp1=dice[1][2] #우측
            temp2=dice[3][1] #하단
            temp3=dice[1][0] #좌측
            temp4=dice[1][1] #중간

            dice[1][2]=temp4
            dice[3][1]=temp1
            dice[1][0]=temp2
            dice[1][1]=temp3
            y=y+1
            x=x
            if maap[x][y]==0:
                maap[x][y]=dice[3][1]
            elif maap[x][y]!=0:
                dice[3][1]=maap[x][y]
                maap[x][y]=0

            return dice[1][1]
        
    elif i==2:
        if 0<=x<n and 0<=y-1<m:
            temp1=dice[1][2] #우측
            temp2=dice[3][1] #하단
            temp3=dice[1][0] #좌측
            temp4=dice[1][1] #중간

            dice[1][2]=temp2
            dice[3][1]=temp3
            dice[1][0]=temp4
            dice[1][1]=temp1
            y=y-1
            x=x

            if maap[x][y]==0:
                maap[x][y]=dice[3][1]
            elif maap[x][y]!=0:
                dice[3][1]=maap[x][y]
                maap[x][y]=0

            return dice[1][1]
        
    elif i==3:
        if 0<=x-1<n and 0<=y<m:
            temp1=dice[0][1] 
            temp2=dice[1][1] 
            temp3=dice[2][1] 
            temp4=dice[3][1]

            dice[0][1]=temp2
            dice[1][1]=temp3
            dice[2][1]=temp4
            dice[3][1]=temp1
            y=y
            x=x-1

            if maap[x][y]==0:
                maap[x][y]=dice[3][1]
            elif maap[x][y]!=0:
                dice[3][1]=maap[x][y]
                maap[x][y]=0
            return dice[1][1]
        

    elif i==4:
        if 0<=x+1<n and 0<=y<m:

            temp1=dice[0][1] 
            temp2=dice[1][1] 
            temp3=dice[2][1] 
            temp4=dice[3][1]

            dice[0][1]=temp4
            dice[1][1]=temp1
            dice[2][1]=temp2
            dice[3][1]=temp3
            y=y
            x=x+1

            if maap[x][y]==0:
                maap[x][y]=dice[3][1]
            elif maap[x][y]!=0:
                dice[3][1]=maap[x][y]
                maap[x][y]=0
            return dice[1][1]
        

n,m,x,y,k=map(int, input().split())

dice=[["",0,""],[0,0,0],["",0,""],["",0,""]]

maap=[]
for i in range(n):
    maap.append(list(map(int, input().split())))

dir=list(map(int, input().split()))

for i in dir:
    result = move(i)
    if result!=None:
        print(result)
    else:
        pass