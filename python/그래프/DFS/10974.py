#10974
#2가지 풀이가 있다.(dfs, permutations)
#1. permutatuions를 이용한 풀이
import itertools 

n=int(input())

for i in itertools.permutations([j for j in range(1,1+n)]):
    #처음에 *을 보고 뭔가 했는데, 여기서 *은 unpacking이라고 한다.
    #unpacking은 여러개의 객체를 포함하고 있는 하나의 객체를 풀어줍니다.
    #즉, 리스트 안의 요소를 꺼내는 역할을 한다.
    print(* i)

'''
이런 방법도 있음
from itertools import permutations #순열 함수

N = int(input())
N_list = [i for i in range(1, N+1)]

for numbers in list(permutations(N_list)):
    for num in numbers:
        print(num, end=' ')
    print()
'''
#그러나 우리는 dfs로 풀줄 아는 것이 더 중요하다.

#2. dfs

n=int(input())

arr=[]

def dfs():
    if(len(arr)==n):
        print(*arr)
        return
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()

dfs()
