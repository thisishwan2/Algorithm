#13164

#첫번째 나의 풀이 맞긴한데 시간초과(이유 for문이 2개여서)
import sys

n,k=map(int, sys.stdin.readline().split())

tall=list(map(int, sys.stdin.readline().split()))

#조마다 티셔츠를 맞추는 비용은 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키 차이만큼 든다
#차이 리스트를 만들어서 큰수 두개를 뺀거를 더하면 답
differ_lst=[]

for i in range(1, len(tall)):
    differ_lst.append(tall[i]-tall[i-1])


for _ in range(k-1):
    differ_lst.remove(max(differ_lst))

print(sum(differ_lst))


#2번째 풀이(정답)
import sys

n,k=map(int, sys.stdin.readline().split())

tall=list(map(int, sys.stdin.readline().split()))

differ_lst=[]

for i in range(1, n):
    differ_lst.append(tall[i]-tall[i-1])

differ_lst.sort()
#n-k개 개수만큼 키차이를 무시할 수 있음. sum해야하므로 슬라이싱
print(sum(differ_lst[:n-k]))