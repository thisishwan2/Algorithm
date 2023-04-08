a, b=input().split()

lst=[]# 겹치지 않는 글자수

cnt=0

if len(a)==len(b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            cnt+=1
    print(cnt)

else:
    if a in b:
        print(0)
    else:
        tri=len(b)-len(a)+1
        for i in range(tri):
            cnt=0
            new=b[i:len(a)+i]
            for i in range(len(a)):
                if a[i]!=new[i]:
                    cnt+=1
            lst.append(cnt)
        print(min(lst))
            
#더 간결한 풀이이다.
a, b = input().split()

answer = []
# for문의 범위를 이렇게 설정해야 길이가 같을때 for문이 작동한다.
# 또한 b의 길이가 a보다 길때 b가 쪼개지는 갯수가 len(b) - len(a) + 1 이다.
# 여기서 b가 쪼개진다는 것은, topcoder-> topco, opcod, pcode, coder 이다.
for i in range(len(b) - len(a) + 1):

    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    #시간을 줄이고 싶으면 위에서 minimum 범위를 잡고. minimum=50
    # if temp < minimum:
    # minimum = temp
    answer.append(count)

print(min(answer))