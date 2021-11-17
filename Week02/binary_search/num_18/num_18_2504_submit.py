import sys
data = sys.stdin.readline().strip()

def par_close(stack, sum_stack, p):
    tmp_sum = 0
    if not stack:
        return -1
    if stack[-1] != p:
        return -1
    if len(sum_stack) == 0: 
        if len(stack) == 1:
            tmp_sum += p
        else :
            sum_stack.append([p, len(stack) - 1])
    else : 
        if len(stack) == 1:
            while sum_stack:
                tmp_sum += sum_stack.pop()[0]
            tmp_sum *= p
        else :
            if sum_stack and sum_stack[-1][1] > len(stack) - 1:
                while sum_stack and sum_stack[-1][1] > len(stack) - 1: 
                    tmp_sum += sum_stack.pop()[0]
                sum_stack.append([p * tmp_sum, len(stack) - 1])
                tmp_sum = 0
            else :
                sum_stack.append([p, len(stack) - 1])
    stack.pop()
    return tmp_sum

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
            if tmp == -1:
                return 0
            else : 
                sum += tmp
    if len(stack) != 0:
        return 0
    return sum

print(parenthesis_value(data))
