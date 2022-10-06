#로직은 어느정도 근접했으나 코드로 풀이를 못함 다시보기
x=int(input())
sum=0           #입력된 사선 라인에서 젤 큰 숫자
cross_line=0    #사선라인
#입력된 사선라인 찾기
while x>sum:
    cross_line+=1
    sum+=cross_line
#입력된 사선라인의 젤 큰수에서 입력된 위치의 차이
gap=sum-x

if cross_line%2==0:         #사선라인이 짝수면
    top=cross_line-gap      #분모는 사선라인과 갭의 차
    under=gap+1             #분자는 갭+1
else:                       #짝수의 반대로
    top=gap+1
    under=cross_line-gap

print("%d/%d" %(top,under))