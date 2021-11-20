import sys, heapq
from collections import deque
from bisect import bisect_left, insort
input = sys.stdin.readline
N = int(input())
#빌딩 정보 받아옵니다. L 좌표 H정보 Y좌표
buildings = deque(list(map(int,input().split()))for _ in range(N))
stack = []
heights = set() #집합
for building in buildings: #building에 값을 넣는데 left, right 좌표 나눠서 
    L, H, R = building
    heights.add((L,-H))
    heights.add((R,H))
ans, heap = [],[0]
before = heap[-1]    
heights=sorted(heights) #x좌표 순으로 정렬
# print(heights)
for P, H in heights:
    if H<0: #왼쪽
        heapq.heappush(heap, -H)
        #insort(heap, -H) #정렬된 상태를 유지하면서 객체룰 추가할 수 있음 
        #print("left", heap)
    else:
        #idx = heap.index(H)
        #heap.pop(idx)
        heap.pop(bisect_left(heap,H)) #
        #print("right", heap)
    if heap[-1] != before:
        ans.append([P, heap[-1]])
        before = heap[-1]
        #print("get", ans, "heap", heap)
    #print("heap:", heap)
for i in range(len(ans)):
    for n in range(2):
        print(ans[i][n],end=' ')



