t=int(input())

for _ in range(t):
    a=list(input().split())
    num=float(a.pop(0))
    for i in range(len(a)):
        if a[i] == '@':
            num=num*3
        elif a[i] == '%':
            num=num+5
        elif a[i] =='#':
            num=num-7
    print("{:.2f}".format(num))