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

visit = []
def BFS(g, start):
    deq = deque()
    deq.append(start)
    while deq:
        item = deq.popleft()
        if item not in visit:
            visit.append(item)
            print(item, end=' ')
            if g.get(item):
                deq.extend(g[item])
    return visit

DFS(graph, V)
print()
BFS(graph, V)
print()

        
        
        
        

#def BFS(g, start, num):
