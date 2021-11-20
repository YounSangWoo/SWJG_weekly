import sys, heapq
from collections import deque
from bisect import bisect_left, insort
input = sys.stdin.readline
N = int(input())
buildings = deque(list(map(int,input().split()))for _ in range(N))
stack = []
heights = set() 
for building in buildings:
    L, H, R = building
    heights.add((L,-H))
    heights.add((R,H))
ans, heap = [],[0]
before = heap[-1]    
heights=sorted(heights)
for P, H in heights:
    if H<0:
        insort(heap, -H) 
    else:
        heap.pop(bisect_left(heap,H)) 
    if heap[-1] != before:
        ans.append([P, heap[-1]])
        before = heap[-1]
for i in range(len(ans)):
    for n in range(2):
        print(ans[i][n],end=' ')



