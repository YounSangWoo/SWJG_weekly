#idx ++ 해가면서 넓이의 max값 찾기 
#폭을 체크할때 현재 최소 높이보다 작아지면 width잘라야함 
#마지막 줄 체크 

import sys
line = []
while True:
    input = map(int, sys.stdin.readline().strip().split())
    line.append(input)
    if input[0] == 0:
        break;

def get_max_histo(num, h):
    if len(h == 1):
        return 1 * h[0]
    cmp = get_max_histo(num - 1, h)
    for i in h:
        

    for idx, h in enumerate(num):
        
        for i in range(n):
            
