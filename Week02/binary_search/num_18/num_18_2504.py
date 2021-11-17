#괄호의 종류가 여러개
#괄호의 종류가 다르면 제대로 닫히지 않음
# () : sole : 2, embed : * 2
# [] : sole : 3, embed : * 3
# XY = X + Y 
# 스택에서 한번 열리면 닫힐때까지 값을 계산해야함 
#닫히는건 처리할 수 있는데 내부에서
#sum_stack은 mul count를 넣어야함 

import sys

data = sys.stdin.readline().strip()
print(data)


def par_close(stack, sum_stack, p):
    tmp_sum = 0
    mul_stack = []
    if not stack or stack[-1] != p:
        return -1
    if len(sum_stack) == 0: #이전 잔여 값이 없는 경우 
        if len(stack) == 1: #하나의 수식이 완성되는 경우
            tmp_sum += p
            print("line23, opt1")
        else : #수식이 아직 완성되지 않은 경우 
            sum_stack.append([p, len(stack) - 1])
            print("line26, opt2")
    else : #이전 잔여 값이 있는 경우 
        if len(stack) == 1: # 하나의 수식이 완성되고, 잔여값이 있는경우 
            while sum_stack:
                tmp_sum += sum_stack.pop()[0]
            print("line 31 opt 3", tmp_sum)
            tmp_sum *= p
        else : #하나의 수식이 완성되지 않고, 잔여값도 남아있는경우 
            if sum_stack and sum_stack[-1][1] > len(stack) - 1:
                while sum_stack[-1][1] > len(stack) - 1: #mul_count 를 넣어주었는데, stack의 인자 기반으로 안애있는 애들을 곱해준다 .
                    tmp_sum += sum_stack.pop()[0] #현재보다 mulcount 큰애들을 다 더해줌 
                sum_stack.append([p * tmp_sum, len(stack) - 1])
                tmp_sum = 0
            else :
                sum_stack.append([p, len(stack) - 1])
            print("line 35 opt 4")
    stack.pop()
    print("tmp_sum", tmp_sum)
    return tmp_sum
#이미 완성됬을 경우는 그냥 더해주면 됨 


def parenthesis_value(p_str):
    stack = []
    sum_stack = []
    status = 0
    sum = 0
    for p in p_str:
        if p == "(" or p == "[":
            if p == "(":
                stack.append(2)
            else:
                stack.append(3)
        else :
            if p == ")":
                tmp = par_close(stack, sum_stack, 2)
            else:
                tmp = par_close(stack, sum_stack, 3)
            print(tmp)
            if tmp == -1:
                return 0
            else : 
                print("check", sum)
                sum += tmp
        print("stack", stack, "sum_stack :", sum_stack, "sum :", sum)
    print("last stack", stack, sum_stack)
    if len(stack) != 0:
        return 0
    return sum

print(parenthesis_value(data))





