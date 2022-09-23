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
    