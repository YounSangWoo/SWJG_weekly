#순서대로 높이가 들어올거고
#n+1이 n 보다 크면 앞에꺼는 필요가 없다. 
#마지막에 len 계산
#뭐에서 틀렸습니다가 뜨지? 

import sys
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))

def higher_stick_num(input):
    stack = []
    for item in input:
        if len(stack) == 0:
            stack.append(item)
        #스택이 비어있을때 그냥 넣어주면되고 
        else :
            if item >= stack[-1]:
                for cmp in stack[::-1]:
                    if cmp <= item:
                        stack.remove(cmp)
                stack.append(item)
            else :
                stack.append(item)
        print(stack)
    return len(stack)

print(higher_stick_num(data))
