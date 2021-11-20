#겹치는 지점의 좌표 
#len(heap) == 0이면 print(0)
#높이가 변하는 순간 : 사각형의 시작, 사각형의 끝
#

import sys
import heapq

n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

def fin_tower(h_heap, end_heap, ret, cur_h):
    tmp = heapq.heappop(end_heap)
    h_heap.remove(((-1) * tmp[2], tmp[1], tmp[0]))
    heapq.heapify(h_heap)
    if len(h_heap) == 0:#힙이 빈경우 -> 바닥
        cur_h = 0
        ret.append([tmp[0], cur_h])
    elif cur_h == tmp[2]:#최대 높이가 end 높이 인 경우  
        cur_h = h_heap[0][0] * (-1)
        ret.append([tmp[0], cur_h])
    return cur_h


def skyline(info):
    info.sort(key = lambda x : x[0])
    #print(info)
    h_heap = []
    end_heap = []
    ret = []
    cur_h = 0
    for square in info:
        while end_heap and end_heap[0][0] < square[0]:
            cur_h = fin_tower(h_heap, end_heap, ret, cur_h)
        heapq.heappush(h_heap, ((-1) * square[1], square[0], square[2]))
        if cur_h < square[1]:
           ret.append([square[0], square[1]])
           cur_h = square[1]
        heapq.heappush(end_heap, (square[2], square[0], square[1]))
    while end_heap:
        cur_h = fin_tower(h_heap, end_heap, ret, cur_h)
    return ret

ans = skyline(data)
for i in ans:
    print(i[0], i[1], end=' ')

