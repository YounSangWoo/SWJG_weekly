import sys

info = list(map(int, sys.stdin.readline().strip().split()))
num = list(sys.stdin.readline().strip())
num_int = list(map(int, num))

def max_removed(info, num):
    tmp = sorted(num_int)
    tmp.reverse()
    print(tmp)
    #for i in range(num):
    #idx 체크해서 num만큼 같을때 최초 max -> 안될 경우 second max
    #idx 만큼 체크해서 그것의 max값 앞에까지 popleft 
    #num 줄여가면서 pop하고 최종 리턴 

    

    return tmp

print(max_removed(info, num))
