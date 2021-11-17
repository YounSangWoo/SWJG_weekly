import sys

n = int(sys.stdin.readline().strip())
p_list = []
for i in range(n):
    p_list.append(list(map(int, sys.stdin.readline().strip().split())))
p_list.sort

def get_distance(p_one, p_two):
    return pow(p_two[0] - p_one[0], 2) + pow(p_two[1] - p_one[1], 2)

def min_point(start, end):
    if start == end:
        return float("inf")
    if end - start == 1: #idx로 생각 
        return get_distance(p_list[start], p_list[end])
    mid = (start + end)//2
    d = min(min_point(start, mid), min_point(mid + 1, end))
    
    target_pos = []
    for i in range(start, end+1):
        if (p_list[mid][0] - p_list[i][0])**2 < d:
            target_pos.append(p_list[i])

    target_pos.sort(key=lambda x: x[1])
    t = len(target_pos)

    for i in range(t-1):
        for j in range(i+1, t):
            if (target_pos[i][1] - target_pos[j][1])**2 < d:
                d = min(d, get_distance(target_pos[i], target_pos[j]))
            else :
                break
    return d

print(min_point(0, n - 1))
