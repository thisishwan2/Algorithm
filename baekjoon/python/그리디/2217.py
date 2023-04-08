
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

#최대 중량 구하는 for문. 무거운 무게부터 1개씩 늘려나감
#ex) w=20 -> maxi=20, w=15,20 -> maxi=30 w=20일때랑 w=15, 20일때 비교 후 더 큰수 저장.
for i in weight_lst:
    a=i*cnt
    maxi=max(maxi,a)
    cnt+=1
print(maxi)