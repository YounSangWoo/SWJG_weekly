import sys
from collections import deque

class Colors:
    RED = '\033[31m'
    BLUE = '\033[34m'
    RESET = '\033[0m'

def turn_dir(d, c):
    if c == "L":
        d = (d - 1) % 4
    else :
        d = (d + 1) % 4
    return d

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
#얘의 인덱스 조절해서 방향조절 

def loop():
    dirc = 1
    time = 1
    y, x = 0, 0
    visited = deque([[y, x]])
    arr[y][x] = 2
    while True:
        y, x = y + dy[dirc], x + dx[dirc]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1:#사과먹을때
                temp_y, temp_x = visited.popleft() #이전 방문지를 뱉어버림 
                arr[temp_y][temp_x] = 0 #방문지 초기화 / 사과를 먹었을 경우는 초기화가 안되고 visited에 꼬리가 들어있다 이후에 앞쪽부터 지워줘야함
            arr[y][x] = 2
            visited.append([y, x])
            if time in times.keys():
                dirc = turn_dir(dirc, times[time])
            time += 1
        else :
            return time
        for i in range (len(arr)):
            if 2 in arr[i]:
                print("[", end="")
                for j in range(len(arr[i])):
                    if arr[i][j] == 2:
                        print(Colors.RED + str(arr[i][j]) + Colors.RESET, end="")
                    elif arr[i][j] == 1:
                        print(Colors.BLUE + str(arr[i][j]) + Colors.RESET, end="")
                    else:
                        print(arr[i][j], end="")
                    if j != len(arr[i]) - 1:
                        print(end=", ")
                    else:
                        print(end="")
                print("]")
            else:
                print(arr[i])
        print(visited)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    arr = [[0] * N for _ in range(N)]
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        arr[a - 1][b - 1] = 1
    L = int(sys.stdin.readline())
    times = {}
    for i in range(L):
        X, C = sys.stdin.readline().split()
        times[int(X)] = C
    print(loop())
