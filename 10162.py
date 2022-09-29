#내가 푼 풀이
T=int(input())

A, B, C=300, 60, 10

AT, BT, CT=0, 0, 0

while True:
    if T>=A:
        T=T-A
        AT+=1
    elif T>=B:
        T=T-B
        BT+=1
    elif T>=C:
        T=T-C
        CT+=1
    elif T==0:
        print(AT, BT, CT)
        break
    else:
        print(-1)
        break
#더 간략한 풀이
T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10
    print(A, B, C)