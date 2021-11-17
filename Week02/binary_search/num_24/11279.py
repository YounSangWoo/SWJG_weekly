#heapq는 최소힙만을 지원하고 최대힙을 쓰려면 reverse flag를 써야함
#    reverse_sign = lambda x: x* (-1)

import heapq
import sys
n = int(sys.stdin.readline().strip())
list = []
for _ in range(n):
    list.append(int(sys.stdin.readline().strip()))

def heap(nums):
    h = []
    for i in nums:
        if i == 0:
            if len(h) != 0:
                print((-1) * heapq.heappop(h))
            else:
                print(0)
        else:
            i = i * (-1)
            heapq.heappush(h, i)
heap(list)
