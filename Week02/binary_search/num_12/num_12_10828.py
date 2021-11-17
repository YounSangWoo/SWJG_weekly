import sys
n = int(sys.stdin.readline().strip())
cmd = []
for i in range(n):
    cmd.append(sys.stdin.readline().strip())
def stack(cmd):
    stack = []
    cmp = ["push", "pop", "size", "empty", "top"]
    for str in cmd:
        if len(str.split()) == 2:
            if str.split()[0] == cmp[0]:
                stack.append(int(str.split()[1]))
        else :
            if str == cmp[1]:
                if len(stack) != 0:
                    print(stack.pop())
                else :
                    print(-1)
            elif str == cmp[2]:
                print(len(stack))
            elif str == cmp[3]:
                if len(stack) == 0:
                    print(1)
                else : 
                    print(0)
            else :
                if len(stack) != 0:
                    print(stack[-1])
                else :
                    print(-1)

stack(cmd)
