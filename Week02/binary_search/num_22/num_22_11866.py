import sys
from collections import deque

#원형큐
#N명에서 k번째 사람을 계속해서 제거
info = list(map(int, sys.stdin.readline().strip().split()))
q = deque()
for i in range(info[0]):
    q.append(i + 1)

def yosepus(q):
    ret = []
    while q:
        q.rotate(-info[1]+1)
        ret.append(q.popleft())
    return ret

list = str(yosepus(q))
#', '.join(list)
print("<" + list[1:-1] + ">")
