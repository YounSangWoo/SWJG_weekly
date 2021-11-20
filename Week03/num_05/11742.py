import sys
N, M = list(map(int, sys.stdin.readline().strip().split()))
input = sys.stdin.readline
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, u, v):
    p_u = find(parent, u)
    p_v = find(parent, v)

    if p_u < p_v:
        parent[p_v] = p_u
    else:
        parent[p_u] = p_v

def count_component(parent, l_num, point_num):
    ele = []
    cnt = 0
    while cnt < l_num:
        pair = list(map(int, input().strip().split()))
        if find(parent, pair[0]) != find(parent, pair[1]):
            union(parent, pair[0], pair[1])
        if not pair[0] in ele:
            ele.append(pair[0])
        if not pair[1] in ele:
            ele.append(pair[1])
        cnt += 1
    p_list = []
    for item in ele:
        p = find(parent, item)
        if not p in p_list:
            p_list.append(p)
    return point_num - len(ele) + len(p_list)

print(count_component(parent, M, N))
