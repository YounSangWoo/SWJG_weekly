import sys

n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
dst = [0] * n


for idx, t in enumerate(tower):
    print(idx, t)
    while stack and tower[stack[-1]] < t:
        stack.pop()
    if stack:
        dst[idx] = stack[-1] + 1
    stack.append(t)

print(' '.join(list(map(str, dst))))


