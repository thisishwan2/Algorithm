import sys

n,m=map(int, sys.stdin.readline().split())
board=[]
count=[]

#n*m 보드판을 입력받아 저장한다.
for _ in range(n):
    board.append(sys.stdin.readline().rstrip())

#보드판에서 시작 점을 잡기 위한 2중 for문이다.
for i in range(n-7):
    for j in range(m-7):
        #8*8 규격이정해졌을때 
        first_W=0  #k,l의 0,0 인덱스가 W로 시작한다고 가정할때, 바꿔야하는 횟수.
        first_B=0  #k,l의 0,0 인덱스가 B로 시작한다고 가정할때, 바꿔야하는 횟수.
        #시작점을 잡았으면 시작점부터 8*8 규격의 요소들을 비교한다.
        for k in range(i,i+8):
            for l in range(j,j+8):
                #현재행 k 와 현재열 l의 합이 짝수면, 시작점과 같은색이고, 홀수면 다른색이다.
                if (k+l)%2==0:
                    if board[k][l]!="W":
                        first_W+=1
                    if board[k][l]!="B":
                        first_B+=1
                else:
                    if board[k][l]!="B":
                        first_W+=1
                    if board[k][l]!="W":
                        first_B+=1
        #'W'로 시작할 경우와 'B'로 시작할 경우 바뀐 체스판의 수 중 작은 수를 count 리스트에 더해준다.
        count.append(min(first_W,first_B))
#모든 경우중 제일 적게 바꾼 수를 출력한다.
print(min(count))
    
