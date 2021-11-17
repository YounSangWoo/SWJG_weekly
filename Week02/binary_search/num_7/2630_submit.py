import math
import sys 
n = int(sys.stdin.readline().strip())
array = []
for i in range (n):
    array += (list(map(int, sys.stdin.readline().strip().split())))

def count_square(array):
    if not 0 in array:
        return [0, 1]
    if not 1 in array:
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
    #얘네를 zip으로 내일합시다 !
    return [x, y]

ans = count_square(array)
print(ans[0])
print(ans[1])

    
