#deque안쓰고인덱스로 큐 구현
import sys
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(sys.stdin.readline().strip().split())

def queue(input):
    cnt = 0
    queue = []
    for cmd in data:
        if cmd[0] == "push":
            queue.append(int(cmd[1]))
        elif cmd[0] == "pop":
            if len(queue) > cnt:
                print(queue[cnt])
                cnt += 1
            else : 
                print(-1)
        elif cmd[0] == "front":
            if len(queue) > cnt:
                print(queue[cnt])
            else: 
                print(-1)
        elif cmd[0] == "back":
            if len(queue) > cnt:
                print(queue[-1])
            else : 
                print(-1)
        elif cmd[0] == "size":
            print(len(queue)-cnt)
        else:
            if len(queue) == cnt :
                print(1)
                cnt = 0
                queue = []
            else :
                print(0)
queue(data)
