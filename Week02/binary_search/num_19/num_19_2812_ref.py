import sys
info = list(map(int, sys.stdin.readline().strip().split()))
num = list(map(int, sys.stdin.readline().strip()))

def get_max(num, info):
    stack = []
    count = info[1]
    i = 0 
    while i <= len(num) - 1: 
        while count and stack and num[i] > stack[-1]: #앞자리 
            stack.pop()
            count -= 1
        stack.append(num[i])
        i += 1
    return stack
print("".join(map(str, get_max(num, info))))



#순서대로 지우는데
#순차적으로 넣는데
#count가 살아있을때 더큰 뒷값이 등장했을 경우 
