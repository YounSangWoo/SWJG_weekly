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
        print("aftre visit", visited)
        #visited가 첫줄 이후로 업데이트가 안되네 
        for dst, pay in enumerate(cost_graph[city]):
            if not dst is city and visited[dst] is False:
                if expense + pay > cur_min :
                    continue
                expense += pay
                visited[dst] = True
                cur_min, expense = self.move_city(cost_graph, visited, dst, expense, cur_min)
                print("line35", expense)
            elif False not in visited and visited[dst] == 'start':
                expense += pay
                if expense < cur_min:
                    cur_min = expense
                print("line35", expense)
                return cur_min, expense
            print("line36", expense)
        return cur_min, expense
    #파이썬은 함수내부에서 값 변경이 안됨 
#방문 도장 찍음
#모두 방문한 경우 재귀를 끝냄
#start를 구분하는 방법
#아예 변수를 다르게 넣는다.
#처음에 start 로직을 넣는다. 
        
    def TSP(self, cost_graph):
        min = pow(10, 6) * n
        for start_city in range(0,n):
            visited = [False for i in range(n)]
            visited[start_city] = 'start'
            min, _  = self.move_city(cost_graph, visited, start_city, 0, min)
            print(min)
        return min

if __name__ == "__main__":
    sol = Solution()
    graph = {}
    for i in range(n):
        graph[i] = data[i]
    print(graph)
    print(sol.TSP(graph))
