import sys
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))

def higher_stick_num(stack):
    if len(stack) == 0:
        return 0 
    max = stack[-1]
    count = 1
    for num in stack[::-1]:
        print(num, max, count)
        if num > max:
            count += 1
            max = num
    return count

print(higher_stick_num(data))
