import sys
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))
print(len(bytes(data)))
count = [0 for i in range(10000)]
for i in data:
    count[i] += 1
for idx, i in enumerate(count):
    while (i):
        print(idx)
        i -= 1
