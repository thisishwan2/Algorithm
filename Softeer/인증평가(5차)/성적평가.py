import sys

#while문 안에서 3번의 대회에 대한 순위를 매김
#이때 학생의 점수와 인덱스를 쌍으로 묶어서 임시배열에 넣고, 정렬
#같으면 rank가 같고, 작으면 직전 rank갯수+rank이다.

n = int(input())    #n = 참가자의 명수

cnt=0
res=[[0 for _ in range(n)]for _ in range(4)]
total=[0]*n
while cnt<3:
    a=list(map(int, input().split()))

    temp=[]
    for i in range(n):
        temp.append([a[i],i])
        total[i]+=a[i]
    temp.sort(reverse=True)

    maxi=sys.maxsize
    rank=0
    rank_cnt=1
    for score, idx in temp:
        if maxi>score:
            rank+=rank_cnt
            rank_cnt=1
            res[cnt][idx]=rank
            maxi=score
        elif maxi==score:
            res[cnt][idx]=rank
            rank_cnt+=1
    cnt+=1


tmp=[]
for i in range(n):
    tmp.append([total[i],i])

tmp.sort(reverse=True)
maxi=sys.maxsize
rank=0
rank_cnt=1
for score, idx in tmp:
    if maxi>score:
        rank+=rank_cnt
        rank_cnt=1
        res[3][idx]=rank
        maxi=score
    elif maxi==score:
        res[3][idx]=rank
        rank_cnt+=1
    cnt+=1

for i in res:
    print(*i)