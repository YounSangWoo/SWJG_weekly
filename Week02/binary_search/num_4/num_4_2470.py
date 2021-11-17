#특성값 : 혼합에 사용된 각 용액의 특성값 
#같은 양의 두 용액을 혼합한 용액의 특성값 
#

import sys
n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))

data.sort()

def get_pair(data):
    left = 0
    right = n-1
    ret = sys.maxsize
    while left < right:
        s_left = data[left]
        s_right = data[right]
        sum = s_left + s_right
        if abs(sum) < ret:
            ret = abs(sum)
            final = [s_left, s_right]
        if sum < 0:
            left += 1
        else:
            right -= 1
    print(final[0], final[1])

get_pair(data)
