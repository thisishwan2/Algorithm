import sys

'''n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split(" ")))

tmp_arr=sorted(set(arr))

zip_list=[]
for i in arr:
    zip=tmp_arr.index(i) #시간복잡도 o(n)
    zip_list.append(zip)

print(" ".join(map(str, zip_list)))'''

import sys

n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split(" ")))

tmp_arr=sorted(set(arr))
dic={}
for i in range(len(tmp_arr)):
    dic[tmp_arr[i]]=i

for i in arr:
    print(dic[i], end=' ')