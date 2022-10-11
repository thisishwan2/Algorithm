a=int(input(""))
b=int(input(""))

c=a*(b%10)
d=a*((b%100)//10)
e=a*(b//100)
f=e*100+d*10+c

print(c)
print(d)
print(e)
print(f)
