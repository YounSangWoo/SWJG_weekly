#append와 pop만
import sys

n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))

def cog(input):
    stack = []
    for num in input:
        if num != 0:
            stack.append(num)
        else:
            stack.pop()
    sum = 0
    for i in stack:
        sum += i
    print(sum)

cog(data)
    

