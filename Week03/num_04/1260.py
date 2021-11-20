import sys
from collections import deque

N, M, V = list(map(int, sys.stdin.readline().strip().split()))
input = sys.stdin.readline
graph = {}

for i in range(M):
    line = list(map(int, input().strip().split()))
    if graph.get(line[0]) == None:
        graph[line[0]] = [line[1]]
    else:
        graph[line[0]].append(line[1])
    if graph.get(line[1]) == None:
        graph[line[1]] = [line[0]]
    else:
        graph[line[1]].append(line[0])
print(graph)

'''
def DFS_self(g, start, num):#간선이 여러개로 로테이션 돌면? 
    if num == 0:
        return
    if visited[start - 1] == True:
        DFS(g, stack.popleft(), num)
        return
    visited[start - 1] = True
    print(start, end=' ')
    temp = g[V]
    i = 0
    while i < len(temp):
        if visited[temp[i] - 1] == False:
            stack.append(temp[i])
        i += 1
    if stack and num != 1:
        DFS(g, stack.popleft(), num - 1)
    return
'''
visited = []
def DFS(g, start):
    visited.append(start)
    print(start, end=' ')
    if g.get(start):
        g[start].sort()
        for node in g[start]: #딕셔너리를 한번에 풀지 않아도 괜찮네
            if node not in visited:
                DFS(g, node)
    return visited

DFS(graph, V)
print()

        
        
        
        

#def BFS(g, start, num):
