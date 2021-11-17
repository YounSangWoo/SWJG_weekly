#열린 괄호를 만나면 stack.append
#닫힌 괄호를 만나면 stack.top해서 일치하면 pop
#닫힌 괄호를 만났는데 스택이 비어있으면 print(NO)
#끝났는데 stack이 남아있으면 printNO 

import sys
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(sys.stdin.readline().strip())

def parenthesis(line):
    stack = []
    cmd = ["YES", "NO"]
    for item in line:
        if item == "(":
            stack.append(item)
        else :
            if len(stack) != 0:
                stack.pop()
            else :
                return cmd[1]
    if len(stack) != 0:
        return cmd[1]
    return cmd[0]

for i in data:
    print(parenthesis(i))

