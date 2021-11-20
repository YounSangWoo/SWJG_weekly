#단 전체 리스트를만들고
#스트라이크 체크 함수 : i
#볼 체크 함수 : 
#brute force인가 그냥? 각 후보에 대해 다 지워버리면 되나 ? 
#일단 입력에 대해 해당 case가 없으면 지워줍시다.
#자릿수가 3개로 픽스라 시간복잡도가 그리 높지 않다.


#123 이랑 모든수랑 전부비교 
#

import sys
n = int(sys.stdin.readline().strip())
data = []
for i in range (n):
    digit = []
    print(i)
    data.append(list(map(int, sys.stdin.readline().strip().split())))
    data[i][0] = [int(data[i][0] / 100), int((data[i][0] % 100) / 10), int(data[i][0] % 10)]
    
class Solution():
    def init_list(self):
        ret = []
        for i in range(1, 9):
            for j in range (1, 9):
                for k in range (1, 9):
                    if i != j and j != k and k != i:
                        ret.append([i, j, k])
        return ret

    def check_count_diff(self, case, cmp, count):
        find = 0

        for i in range(3):
            if case[i] in cmp:
                find += 1
        if find == count:
            return False
        else: 
            return True

    def delete_not_contain(self, list, input):
        for line in input:
            for case in list:
                if (self.check_count_diff(case, line[0], line[1] + line[2])):
                    list.remove(case)
    #위에 한번 지우고 해봐야겠네 이게 사실상 ball count 

    def strike_match(self, case, cmp, count):
        find = 0
        for i in range(3):
            if case[i] == cmp[i]:
                find += 1
        if find == count:
            return True
        else:
            return False

    def delete_not_match(self, list, input):
        for line in input:
            for case in list:
                if self.strike_match(case, line[0], line[1]) == False:
                    list.remove(case)
        
    def get_count(self, list, question):
        #num은 
        match_dic = {}
        for num in list:
            match_dic[tuple(num)] = []
            for line in question:#json으로 넘길때는 명시적인 형태가 필요 없다. 
                s_count = 0
                b_count = 0
                cmp = line[0]
                s_cmp = line[1]
                b_cmp = line[2]
                for i in range (3):
                    print("check", num[i], cmp[i])
                    if num[i] == cmp[i]:
                        s_count += 1
                    elif num[i] in cmp:
                        b_count += 1
                match_dic[tuple(num)].append([s_count, b_count]) 
                #if s_count != s_cmp or b_count != b_cmp:
                 #   list.remove(num)
                #if b_count != question[1] :
                #   del_flag = 1
                #print(num, line)
        print(match_dic)
        
        

if __name__ == "__main__":
    sol = Solution()
    list = sol.init_list()
   # print("before", list)
    sol.delete_not_contain(list, data)
   # print("after", list)
    sol.delete_not_match(list, data)
    print("after", list)
    sol.get_count(list, data)
    print("sol", list)
