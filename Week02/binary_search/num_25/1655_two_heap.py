import heapq
import sys
n = int(sys.stdin.readline().strip())
input = sys.stdin.readline #이러면 함수명까지 저장되고 함수는 실행 안되는건가 ?
#힙 두개 써서 카운팅 ㅎ ㅏ지말고 max heap의 최대값을 꺼내봅시다. 
def spit_middle(n):
    max_h = []
    min_h = []
    for i in range(n):
        if len(max_h) > len(min_h):
            heapq.heappush(min_h, int(input()))
        else:
            heapq.heappush(max_h, int(input()) * (-1))
        if min_h and max_h[0] * (-1) > min_h[0]:
            tmp1, tmp2 = heapq.heappop(min_h), heapq.heappop(max_h)
            heapq.heappush(max_h, tmp1 * (-1))
            heapq.heappush(min_h, tmp2 * (-1))
        print(max_h[0] * (-1))
    return 

spit_middle(n)

