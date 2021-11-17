import sys

tree_num, min_sum = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().strip().split())) 

def get_left_tree(data):
    data.sort()
    start, end = 1, data[-1]
    while start <= end:
        mid = (start + end)//2
        cur_sum = 0
        for i in data:
            if i >= mid:
                cur_sum += i - mid
        if cur_sum >= min_sum:
            start = mid + 1
        else :
            end = mid - 1
    print(end)
    

get_left_tree(data)

'''
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2

    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid

    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
'''
