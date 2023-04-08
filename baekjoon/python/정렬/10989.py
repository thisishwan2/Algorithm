#메모리가 8mb 인 문제

import sys

n=int(sys.stdin.readline())
#문제에서 주어진 값의 범위는 10000보다 작거나 같은 자연수이므로
#미리 10000개의 빈 리스트를 만들어준다.
#그러나 인덱스는 0부터 세기 때문에 이를 계산하기 편하게 길이가 10001인 리스트를 만든다.
num_list=[0]*10001

for _ in range(n):
    #입력받는 수를 인덱스로 바꾸어서 해당하는 숫자의 인덱스에 1을 더해준다.
    num_list[int(sys.stdin.readline())]+=1

for i in range(10001):
    if num_list[i]!=0:  #빈 리스트가 아니먄 == 입력받은 숫자가 있는
        for j in range(num_list[i]):    #(i번째 인덱스 = 입력받은 숫자)가 위에서 +=1 된 횟수만큼 범위로 지정 
            print(i)    #횟수만큼 출력(중복으로 받은 수를 출력하기 위해서)
