#숫자 작은 애들 순으로 빼서 합치고 넣고 합치고 넣고 

import heapq
import sys

n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))

def min_count(data):
    h = []
    sum = 0
    for i in data:
        heapq.heappush(h, i)
    while len(h) >= 2:
        tmp1 = heapq.heappop(h)
        tmp2 = heapq.heappop(h)
        sum += tmp1+tmp2
        heapq.heappush(h, tmp1+tmp2)
    print(h)
    return sum
print(min_count(data))

