import sys
#사이클은 중간에서 생길수도 있다. 항상 체크해주면 시간복잡도가 너무 커짐 

V, E = list(map(int, sys.stdin.readline().strip().split()))
line = []
for i in range(E):
    line.append(list(map(int, sys.stdin.readline().strip().split())))
parent = [0] * (V + 1)
edges = []
result = 0


#Union-find
#find 함수 : 전체 집합을 넣고 parent를 계속 찾아줌

#Union : 작은 루드 노트를 기준으로 합침 -> 다른 애들을 합치는건데 유니온은 여기서 필요 없을듯

def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

g = [i for i in range(V)]
tree = {}

for i in range(1, v + 1):
    parent[i] = i


def min_span_tree(p_num, l_num, l_info):
    result = []

print(g)
def min_span_tree(p_num, l_num, l_info):
    l_info.sort(key = lambda a: a[2])
    #정렬 ok print(l_info)
    #유니온 파인드는 일단 다 찾고 나서
    #크루스칼 알고리즘이 모든 경우 다찾는건가 ? 
    #순서대로 돌리면 알고리즘 시간복잡도 n
    #거기에 유니온 파인드
    result = []
    for item in l_info:
        if not tree.get(item[0]):
            tree[item[0]] = [item[1], item[2]]
        else:
            tree[item[0]].append([item[1], item[2]])
    for lst in trees:

    print(tree)
    for item in l_info:
        l_info.append()
     
           
min_span_tree(V, E, line)

'''
    while cnt kk< V:
        line = l_info[0]
        end = l_info[1]
'''

#min_span_tree(V, E, line)
#EOF error
