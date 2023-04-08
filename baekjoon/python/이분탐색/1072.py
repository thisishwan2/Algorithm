#1072

import sys
input=sys.stdin.readline

x,y=map(int, input().split())
z=y*100//x

if z>=99:
    print(-1)
else:
    #범위를 아예 총 게임 횟수로 잡아버린다.
    start=1
    end=1000000000
    ans=0


    while start <= end:
        mid=(start+end)//2

        if (y+mid)*100//(x+mid) >z:
            end=mid-1
            ans=mid
        else:
            start=mid+1
    print(ans)
#
#
# import sys
# input=sys.stdin.readline
#
# x,y=map(int, input().split())
# z=y*100//x
#
# lst=list(range(x-y+1))
#
# def lower(start, end,init_per,lst):
#     while start<=end:
#         mid=(start+end)//2
#
#         if ((y+mid)*100)//(x+mid) > init_per:
#             a=mid
#             end=mid-1
#         else:
#             start=mid+1
#     return end
#
# if z>=99:
#     print(-1)
# else:
#     print(lower(0,lst[-1],z,lst))