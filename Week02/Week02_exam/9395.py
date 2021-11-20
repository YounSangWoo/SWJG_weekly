
'''
def after_bum(line, bum_str):#에외 찾는게 의미가 있을까 싶긴 하네 
    stack = []
    i = 0
    while i < len(line):
        if line[i] == bum_str[0]: #첫문자 체크 
            if i + len(bum_str) <= len(line) and line[i: i + len(bum_str)] == bum_str: #이후 문자열이 일치하는지 확인
                i += len(bum_str) #일치할 경우 index 점프
                while i < len(line): #idx가 line을 넘어갈 경우 제외 
                    if line[i] in bum_str: 
                        right = bum_str[bum_str.index(line[i]):]#
                        left = bum_str[:bum_str.index(line[i])]
                        if i + len(right) <= len(line) and len(stack) >= (len(bum_str) - len(right)):
                            if right == line[i:i + len(right)] and left == stack[len(stack) - (len(bum_str) - len(right)):]:
                                stack = stack[: len(stack) - (len(bum_str) - len(right))]
                        i += len(right)
                    else : 
                        break
            else :
                stack.append(line[i])
                i += 1
        else :
            stack.append(line[i])
            i += 1
    if len(stack) == 0:
        print("FRULA")
    else:
        print(''.join(stack))
    return
'''
import sys
input_line = sys.stdin.readline().strip()
bum_string = sys.stdin.readline().strip()

def after_bump(line, bum_str):
    stack = []
    bum_str = list(bum_str)
    for char in line:
        stack.append(char)
        if len(stack) >= len(bum_str) and stack[-len(bum_str):] == bum_str:
            for j in range(len(bum_str)):
                del stack[-1]
    if len(stack) == 0:
        return "FRULA"
    return ''.join(stack)
            
print(after_bump(input_line, bum_string))
