#일단 범위에 따라 4개로 분할하는 알고리즘
#check_unity
import math
import sys 
n = int(sys.stdin.readline().strip())
array = []
for i in range (n):
    array += (list(map(int, sys.stdin.readline().strip().split())))

print(array)


def count_square(array):
    if not 0 in array:
        print("case1", array)
        return [0, 1]
    if not 1 in array:
        print("case2", array)
        return [1, 0]
    unit = int(math.sqrt(len(array))/2)
    div_array = [[], [], [], []]
    for idx, ele in enumerate(array):
        if idx % (2 * unit) < unit  and idx < 2 * unit * unit:
            div_array[0].append(ele)
        elif idx % (2 * unit) >= unit and idx < 2 * unit * unit:
            div_array[1].append(ele)
        elif idx % (2 * unit) < unit and idx >= 2 * unit * unit:
            div_array[2].append(ele)
        else :
            div_array[3].append(ele)
    each_list = [count_square(div_array[i]) for i in range(4)]
    x = each_list[0][0] + each_list[1][0] + each_list[2][0] + each_list[3][0]
    y = each_list[0][1] + each_list[1][1] + each_list[2][1] + each_list[3][1]
    #여기 수정하고, 에러케이스 뭐지? 
    return [x, y]
    #얘네가 나눠지는 위치는 각자 다름 
    #리턴은 결국 값을 돌려주는 것 


'''
    s_unit = 0
    e_unit = unit
    div_array = []
    for i in range(unit):
        div_array += array[s_unit:e_unit]  
        s_unit, e_unit = s_unit + 2 * unit, e_unit + 2 * unit
'''
   #return count_square([:N/2:N/2]) 
    #for i in range(4):
    #조건문으로 순서대로 만들어서 4열짜리 이중배열


print(count_square(array))
