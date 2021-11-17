import sys
from collections import deque

def turn_dir(d, c):
    if c == "L":
        d = (d - 1) % 4
    else :
        d = (d + 1) % 4
    return d

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def loop():
    dirc = 1
    time = 1
    y, x = 0, 0
    visited = deque([[y, x]])
    arr[y][x] = 2
    while True:
        y, x = y + dy[dirc], x + dx[dirc]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1:
                temp_y, temp_x = visited.popleft() 
                arr[temp_y][temp_x] = 0
            arr[y][x] = 2
            visited.append([y, x])
            if time in times.keys():
                dirc = turn_dir(dirc, times[time])
            time += 1
        else :
            return time

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
