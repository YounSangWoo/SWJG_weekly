import sys
import heapq

n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    temp = sorted(list(map(int, sys.stdin.readline().strip().split())))
    data.append(temp)
data.sort(key=lambda x: x[1])
t_len = int(sys.stdin.readline().strip())

def get_train_place(commuter, l):
    h = []
    p_max = -1
    for cmt in commuter:
        range = cmt[1] - l 
        if range <= cmt[0]:
            heapq.heappush(h, cmt[0])
        while h and range > h[0]:
            heapq.heappop(h)
        p_max = max(p_max, len(h))
    return p_max
print(get_train_place(data, t_len))

#우선순위 큐 이용
#sort 후에 순서대로 넣고 
#end순으로 뺸다 

#내가 원래 하던 방식은 새로운 점이 나오면 시작점에  L을 빼서 범위 밖의 애들을 pop하고, max업데이트, 새로운 애들을 집어넣는 형태
#sol은 새로운 점이 나오면 그 점의 끝점에서 l을 뺴서 range를 잡고 range 밖의 점들을 버린다. if문으로 새롭게 들어오는 애들도 체크 가능 
#sorted를 집약적으로 사용가능
#
