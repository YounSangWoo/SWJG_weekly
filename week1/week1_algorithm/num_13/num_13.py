import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
    
class Solution:
    def get_average(self, list):
        avg = 0
        num_list = list[1:]
        for i in num_list:
            avg += i
        return avg/list[0]  

    def get_percent(self, data):
        ret = []
        for list in data:
            cnt = 0
            average = self.get_average(list)
            num_list = list[1:]
            for grade in num_list:
                if grade > average:
                    cnt += 1
            ret.append(cnt/list[0]) 
        return ret
        
if __name__ == "__main__":
    sol = Solution()
    per_list = sol.get_percent(data)
    for i in per_list:
        print("{:.3f}%".format(100 * i))
