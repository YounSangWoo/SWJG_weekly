import math, sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def init(arr, tree, node, start, end):
    if start == end:
        tree[node-1] = start
    else:
        mid = (start + end)//2
        init(arr, tree, node*2, start, mid)
        init(arr, tree, node*2+1, mid+1, end)

        if arr[tree[node*2-1]] < arr[tree[node*2]]:
            tree[node-1] = tree[node*2-1]
        else :
            tree[node-1] = tree[node*2]

def query(arr, tree, node, start, end, x, y):
    if x > end or y < start:
        return -1
    if start >= x and end <= y:
        return tree[node-1]
    mid = (start+end)//2
    left = query(arr, tree, node*2, start, mid, x, y)
    right = query(arr, tree, node*2+1, mid+1, end, x, y)

    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        if arr[left] >= arr[right]:
            return right
        else:
            return left

def dac(start, end):
    index = query(arr, tree,1, 0, len(arr)-1, start, end)
    if abs(end-start)==0:
        return arr[index]

    v1,v2,v3 = arr[index] * (end-start+1),0,0

    if index-1 >= start:
        v2 = dac(start,index-1)
    if index+1 <= end:
        v3 = dac(index+1,end)

    return max(v1,v2,v3)

while (True):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        break

    n = temp[0]
    arr = temp[1:]
    tree = [0]*(pow(2,math.ceil(math.log(len(arr), 2))+1)-1)

    init(arr,tree,1,0,len(arr)-1)
    print(dac(0,len(arr)-1))
