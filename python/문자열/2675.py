t=int(input(""))

for i in range(t):
    r, s = map(str, input().split())
    r=int(r)
    l=len(s)
    p=""
    for j in range(l):
        p=p+s[j]*r      #문자열 s의 각 인덱스 마다 r을 곱하여 p에 저장

    print(p)

    
