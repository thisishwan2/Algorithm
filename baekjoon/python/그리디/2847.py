n=int(input())

score = []
for _ in range(n):
    score.append(int(input()))

answer = 0
prev_score = score[-1]
for i in range(len(score)-2,-1,-1):
    if score[i]>=prev_score: # 점수는 본인 다음 점수보다 1작아야 좋다.
        answer+=score[i]-prev_score+1
        score[i]=prev_score-1
        prev_score = score[i]
    else:
        prev_score = score[i]
print(answer)