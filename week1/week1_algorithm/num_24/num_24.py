#가로: x, 세로: y
#종이와 가로와 세로의 길이 
#
#
import sys
square_info = list(map(int, sys.stdin.readline().strip().split()))
#map은 map 객체를 만들기 때문에 리스트로 받기위해서는 list()로 형변환
#list(int(sys.stdin.readline().strip().split()))
#두개의 정수 리스트가 결과 
#readline, split, convert_int, 
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

class Solution:
    #make_square
    #divide_square
    #입력이 들어올때마다 잘라야함
    #main
    #main에서 row, column을 받고
    #row, col
    #input 이 들어온다 
    #각 리스트 별로 범위에 해당하는지 알아야함 
    #[(0,0), (2, 4)] if 1 : x, 0 : y 
    def divide_apply_square(self, square, flag, cut_place):
        #해당하는 케이스만 들어옴 
        ret = []
        left_top = square[0]
        right_bottom = square[1]
        if flag == 1: #about x
            div_square_one = [(left_top[0], left_top[1]), (cut_place, right_bottom[1])]
            div_square_two = [(cut_place, left_top[1]), (right_bottom[0], right_bottom[1])]
        else : #about y 
            div_square_one = [(left_top[0], left_top[1]), (right_bottom[0], cut_place)]
            div_square_two = [(left_top[0], cut_place), (right_bottom[0], right_bottom[1])]
        ret.append(div_square_one) 
        ret.append(div_square_two)
        return ret 

    def check_inrange_square(self, square, flag, cut_place):
        if flag == 1:
            if cut_place >= square[0][0]  and cut_place <= square[1][0]:
                return 1
        elif flag == 0:
            if cut_place >= square[0][1] and cut_place <= square[1][1]:
                return 1
        return 0

    def get_area(self, point_list):
        area_list = []
        for item in point_list:
            area = (item[1][0] - item[0][0]) * (item[1][1] - item [0][1])   
            #동일한 리스트와, 동일한 좌표 성분 이런식으로 생각해얒 
            area_list.append(area)
        return area_list

if __name__== "__main__":
    sol = Solution()
    row = square_info[0]
    col = square_info[1]
    full_square = [(0, 0), (square_info[0], square_info[1])]
    square_list = [full_square]
    for cut_info in data:
        new_list = []
        pop_idx_list = [] 
        #pop 은 루프 한번 돌리고 이루어져야함 
        for idx, each_square in enumerate(square_list):
            if (sol.check_inrange_square(each_square, cut_info[0], cut_info[1])):
                pop_idx_list.append(idx)
                new_list += sol.divide_apply_square(each_square, cut_info[0], cut_info[1])
        pop_idx_list.reverse()
        for idx in pop_idx_list: #idx 혼동을 방지하기 위해 분리 
            square_list.pop(idx)     
            #이거전체적으로 
        square_list += new_list
    print(square_list)
    area_list = sol.get_area(square_list)
    print(max(area_list))    

            
            #두가지 1. pop 특정 square, 2. list 이어 붙이기 
                






    
