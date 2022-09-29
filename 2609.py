#유클리드 호재법
m,n=map(int, input().split())
mini=m*n
while True:
    if n!=0:
        a=n
        b=m%n
        m,n=a,b
    else:
        max=a
        break
    
min=mini//max
print(max)
print(min)

"""
A, B = map(int,input().split())
a, b = A, B

while b != 0:
    a = a % b
    a, b = b, a

# gcd
print(a)

#lcm
print(A*B//a)

"""