import sys
from collections import deque

n = int(sys.stdin.readline().strip())
q = deque()
for i in range(n):
    q.append(i + 1)

def get_last_card(q):
    while len(q) > 1:
        q.popleft()
        q.append(q.popleft())
    return q[0]

print(get_last_card(q))
