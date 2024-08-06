n=int(input())

stack=[]
for _ in range(n):
    cmd = input().split()

    # push
    if len(cmd)==2:
        stack.append(cmd[1])

    elif cmd[0] == "pop":
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0]=="top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])