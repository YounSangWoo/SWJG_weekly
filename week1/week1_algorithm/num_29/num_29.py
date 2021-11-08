# 오름차순 정렬
#선택 정렬 :  
#리스트를 나누는 방식도 의미가 있나 ? 

import sys 
n = int(sys.stdin.readline().strip())
data = []
for i in range (n):
    data.append(int(sys.stdin.readline().strip()))

class Solution:
    def get_mid_piv(self, pivot_select):
        comp_list = sorted(pivot_select)
        if com_list[1] == pivot_select[0] :
            return 0
        elif com_list[1] == pivot_select[1]:
            return 1
        else com_list[1] == pivot_select[2]
            return 2 

    def quick_sort(self, list):
        if len(list) == 0:
            return []
        elif len(list) == 1:
            return list
        elif len(list) == 2:
            if list[0] > list[1]:
                list[0], list[1] = list[1], list[0]
            return list
        piv_idx = self.get_mid_piv(list[0:3])
        for i in list:
            if i <= piv_value:
                left.append(i)
            else:
                right.append(i)
        return self.quick_sort(left) + self.quick_sort(right)
        
if __name__== "__main__":
    sol = Solution()
    sorted_list = sol.quick_sort(data)
    for num in sorted_list:
        print(num)


