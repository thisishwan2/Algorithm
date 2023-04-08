import sys

n=int(sys.stdin.readline())

#즉, 666앞의 숫자가 6을 넘기 전후로 변화가 있음.
#666앞의 수가 6을 넘기전에는 666 앞에서 수를 올리고, 넘으면 666뒤에서 0부터 다시 카운트
#하지만 이런 규칙을 이용해서 푸려고 하면 너무 어렵고 복잡하다.
#따라서 우리는 숫자 666부터 1씩증가시키면서 그 숫자마다 666이 들어있는지를 확인할것이다.
#우리가 지정한 횟수만큼 666이 포함된것을 카운트 했을때 나오는 값이 답이다.

cnt=0
sixsixsix=666

while True:
    if "666"in str(sixsixsix):
        cnt+=1
    if cnt==n:
        print(sixsixsix)
        break
    sixsixsix+=1
