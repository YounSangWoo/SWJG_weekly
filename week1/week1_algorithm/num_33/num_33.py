# ele_sum = 100 
# 정답이 여러가지면 아무거나 
# 항상 100이 되는 조합은 있음
# 오름차순 정렬

import sys
data = []
for i in range(9):
    data.append(int(sys.stdin.readline().strip()))

class Solution:
    def find_fake(self, list, over_num):
        for idx, i in enumerate(list):
            pair = over_num - i
            if pair in list and list[idx] is not pair:
                list.remove(i)
                list.remove(pair)
                return list

if __name__ == "__main__":
    sol = Solution()
    sum = 0
    for i in data:
        sum += i
    over_num = sum - 100 
    ans = sorted(sol.find_fake(data, over_num))
    for i in ans:
        print(i)
