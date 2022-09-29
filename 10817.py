list =list(map(int, input().split()))
a=sorted(list)
print(a[1])

# "if 로 풀어보자" sort함수는 변수에 저장하지 않고 list.sort()처럼 쓰고, sorted(list)는 변수에 저장해서 씀.
'''
a,b,c=map(int, input().split())
if a>=b:
    if a>=c:
        if b>=c:
            print(b)
        else: 
            print(c)
    else:
        print(a)
else:
    if b>=c:
        if a>=c:
            print(a)
        else: 
            print(c)
    else:
        print(b)
        '''