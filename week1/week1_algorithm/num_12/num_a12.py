import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]


class Solution:
    def get_each_point(self, data):
        list = []
        for line in data:
            point = 0
            cur_point = 1
            for OX in line:
                if OX == "O":
                    point += cur_point
                    cur_point = cur_point + 1
                elif OX == "X":
                    cur_point = 1
            list.append(point)
        return list

if __name__ == "__main__":
  sol = Solution()
  point_list = sol.get_each_point(data)
  for point in point_list:
    print(point)
