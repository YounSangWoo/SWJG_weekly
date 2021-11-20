import sys
from itertools import permutations
n = int(sys.stdin.readline().strip())
data = []

for i in range (n):
    digit = []
    data.append(list(map(int, sys.stdin.readline().strip().split())))
    data[i][0] = [int(data[i][0] / 100), int((data[i][0] % 100) / 10), int(data[i][0] % 10)]
    
class Solution():
    def check_question(self, tuples, match_dic, question):
        ret = []
        for item in tuples:
            flag = 1
            cmp_list = match_dic[item]
            for idx, line in enumerate(question):
                if cmp_list[idx] != [line[1], line[2]]:
                    flag = 0
            if flag == 1:
                ret.append(item)
        return len(ret)
    
    def get_count(self, lists, question):
        match_dic = {}
        for item in lists:
            match_dic[item] = []
            for line in question:
                s_count = 0
                b_count = 0
                cmp = line[0]
                s_cmp, b_cmp = line[1], line[2]
                for i in range (3):
                    if item[i] == cmp[i]:
                        s_count += 1
                    elif item[i] in cmp:
                        b_count += 1
                match_dic[item].append([s_count, b_count]) 
        ret = self.check_question(list(lists), match_dic, question)
        return ret
        
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lists = list(permutations(nums, 3))
    print(sol.get_count(lists, data))

