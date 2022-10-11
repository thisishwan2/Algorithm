n=int(input())
han=0

if n<100:
    han=n
else:
    han=99
    for i in range(100,n+1):
        i=str(i)
        if (int(i[0])+int(i[2]))/2==int(i[1]):
            han+=1

print(han)

#다른 풀이
num = int(input())

hansu = 0
for i in range(1, num+1):
    num_list = list(map(int, str(i)))       #map(int, str(i)) : 문자열로 되어있는 각 자릿수를 정수로 바꿔준다( ex, "123" > 정수 1, 2, 3 각각으로 바꿔준다)
    if i < 100:
        hansu += 1  # 100보다 작으면 모두 한수
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu += 1  # x의 각 자리가 등차수열이면 한수
print(hansu)
