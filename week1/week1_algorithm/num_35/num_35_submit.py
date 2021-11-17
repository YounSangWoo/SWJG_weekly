import sys
import math
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

class Solution:
    def move_city(self, cost_graph, visited, city, sum):
        for dst, pay in enumerate(cost_graph[city]):
            if not dst is city and visited[dst] is False:
                if sum[1] + pay > sum[0] or pay == 0:
                    continue
                sum[1] += pay
                visited[dst] = True
                self.move_city(cost_graph, visited, dst, sum)
            elif False not in visited and visited[dst] == 'start':
                sum[1] += pay
                if sum[1] < sum[0]:
                    sum[0] = sum[1]
                return True
        return False
        
    def TSP(self, cost_graph):
        min = pow(10, 6) * n
        init_sum = [min, 0]
        
        for start_city in range(0,n):
            visited = [False for i in range(n)]
            visited[start_city] = 'start'
            init_sum[1] = 0
            self.move_city(cost_graph, visited, start_city, init_sum)
        return init_sum[0]

if __name__ == "__main__":
    sol = Solution()
    graph = {}
    for i in range(n):
        graph[i] = data[i]
    print(sol.TSP(graph))
