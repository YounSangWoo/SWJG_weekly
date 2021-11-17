import sys

n = int(sys.stdin.readline().strip())
tower = list(map(int, sys.stdin.readline().strip().split()))
stack = []
dst = [0] * n

for i in range(n):
    t = tower[i]
    while stack and tower[stack[-1]] < t:
        if tower[stack[-1]] < t:
            stack.pop()
    if stack:
        dst[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, dst))))

