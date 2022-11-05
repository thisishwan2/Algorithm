
#2217
import sys
n=int(sys.stdin.readline())

weight_lst=[]

for _ in range(n):
    weight=int(sys.stdin.readline())
    weight_lst.append(weight)

weight_lst.sort(reverse=True)
cnt=1
maxi=0
for i in weight_lst:
    a=i*cnt
    maxi=max(maxi,a)
    cnt+=1
print(maxi)