import sys
from collections import deque

n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(list(map(str, sys.stdin.readline().strip().split())))
root = data[0][0]

def init_graph(list):
    dict = {}
    for line in list:
        dict[line[0]] = [line[i] for i in range(1,3)]
    return dict

def preorder(g, root):
    dec = deque()
    dec.append(root)
    while dec:
        item = dec.popleft()
        print(item, end='')
        node = g[item]
        if node[0] != '.' and node[0] not in dec:
            dec.appendleft(node[0])    
        if node[1] != '.' and node[1] not in dec:
            dec.append(node[1])
    print()
    return 

def inorder(g, root):
    dec = deque()
    dec.append(root)
    while dec:
        item = dec[-1]
        node = g[item]
        #왜안들어가지? 
        #C A B 이렇게 들어가지 않나? 
        #print(dec)
        if node[0] == '.' and node[1] == '.':
            print(dec.pop(), end='')
            while dec:
                item = dec[-1]
                node = g[item]
                if node[1] == '.' or node[1] in dec:
                    print(dec.pop(), end='')
                else :
                    break
            continue
        elif node[0] in dec or node[1] in dec:
            print(dec.pop(), end='')
            continue
        if node[1] != '.' and node[1] not in dec:
            dec.appendleft(node[1])
        if node[0] !=  '.'and node[0] not in dec:
            dec.append(node[0])
    print()
    return

def postorder(g, root):
    dec = deque()
    dec.append(root)
    while dec:
        if len(dec) != 1 and dec[0] == root:
            flag = -1
        else:
            flag = 0
        item = dec[flag]
        node = g[item]
        if node[0] != '.' and node[0] not in dec:
            dec.appendleft(node[0])
        if node[1] != '.' and node[1] not in dec:
            dec.append(node[1])
        if node[0] == '.' and node[1] == '.':
            while dec[flag] != root:
                if flag == 0:
                    print(dec.popleft(), end='')
                else:
                    print(dec.pop(), end='')
        if len(dec) == 1 and dec[0] == root:
            print(dec.pop(), end='')
    print()
    return
            
graph = init_graph(data)
preorder(graph, root)
inorder(graph, root)
postorder(graph, root)
