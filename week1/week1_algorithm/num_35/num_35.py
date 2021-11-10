# TSP
#도시들이 있고 도시들 사이에는 길이 있음
#그래프
#모든 도시를 다 돌아야함  
#한바퀴 돌아서 원래의 도시로 
#dfs, backtracking

#시작점도 마음대로 선택할 수 있다
#min을 리스트로 할 필요는 없다
#파라미터로 left_city 변수를 넘겨줘야함

import sys
import math
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

class Solution:
    def move_city(self, cost_graph, visited, city, expense, cur_min):
        #그래프 그냥 n 개수 만큼 루프 돌리면 됨 
        #print("aftre visit", visited)
        #visited가 첫줄 이후로 업데이트가 안되네 
        '''
        if False not in visited:
            print("if inside?")
            if expense < cur_min:
                 print("value chg", cur_min, expense)
                 cur_min = expense
                 return cur_min
        '''
        for dst, pay in enumerate(cost_graph[city]):
            if not dst is city and visited[dst] is False:
                if expense + pay > cur_min :
                    continue
                expense += pay
                visited[dst] = True
                cur_min = self.move_city(cost_graph, visited, dst, expense, cur_min)
            elif False not in visited and visited[dst] == 'start':
                expense += pay
                if expense < cur_min:
                    cur_min = expense
                return cur_min
        return cur_min 
#방문 도장 찍음
#모두 방문한 경우 재귀를 끝냄
#start를 구분하는 방법
#아예 변수를 다르게 넣는다.
#처음에 start 로직을 넣는다. 
        
    def TSP(self, cost_graph):
        #visited = [False for i in range(n)]
        min = pow(10, 6) * n
        #visited = [False for i in range(n)]
        for start_city in range(0,n):
            visited = [False for i in range(n)]
            visited[start_city] = 'start'
            min = self.move_city(cost_graph, visited, start_city, 0, min)
        return min

if __name__ == "__main__":
    print(data)
    list = []
    list.append(True)
    list.append(11)
    list.append("test")
    print(list)
    sol = Solution()
    graph = {}
    for i in range(n):
        graph[i] = data[i]
    print(graph)
    print(sol.TSP(graph))
