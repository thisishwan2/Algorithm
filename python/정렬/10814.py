import sys

n=int(sys.stdin.readline())
join=[]
for _ in range(n):
    a,b = map(str, sys.stdin.readline().rstrip().split(" "))
    a=int(a)
    join.append([a,b])
join.sort(key=lambda x: (x[0]))

for i in range(n):
    print(join[i][0], join[i][1])

#다른 풀이
import sys
N=int(sys.stdin.readline())

arr=[]

for i in range (N): 
  a,b = map(str,sys.stdin.readline().split()) 

  arr.append([int(a), i, b]) #여기에 i를 추가함.
#i추가 이유는 입력 받은 순서대로 정렬하기 위해

arr.sort()
for i in range (len(arr)): 
  print("%d %s"%(arr[i][0], arr[i][2]))