t=int(input())

for _ in range(t):
    a=list(input())
    score=0                     
    score_sum=0                 #새로운 a리스트를 입력받으면 점수 합계를 리셋
    for i in a:
        if i=="O":
            score+=1            #O가 연속되면 점수가 1씩커짐
            score_sum+=score    #1+2+0+0...을 표현하는 방법
        else:
            score=0             #X면 리셋
    print(score_sum)