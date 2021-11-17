#중간값, 짝수면 두개 중에서 작은수
#힙 하나에서 len의 절반만큼 빼면되나 ?
#cnt % 2 == 0 -> cnt/2
#cnt %2 == 1 -> cnt/2 + 1 
#최소힙 최대힙 두개를 써야하나 ? 

import heapq
import sys
n = int(sys.stdin.readline().strip())

def spit_middle(n):
    h = []
    for i in range(n):
        if (i + 1) % 2 == 0 : 
            count = (i + 1)//2
        else :
            count = (i + 1)//2 + 1
        h.append(int(sys.stdin.readline().strip()))
        tmp = h[:]
        heapq.heapify(tmp)
        while count > 1:
            heapq.heappop(tmp)
            count -= 1
        print(heapq.heappop(tmp))

spit_middle(n)
