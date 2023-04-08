i=0
s1=set([])
while i<10:
    a=int(input())
    b=a%42
    s1.add(b)
    i+=1
l1=list(s1)
print(len(l1))

#다른 풀이
s = set()
for i in range(10):
    s.add(int(input())%42)
print(len(s))
