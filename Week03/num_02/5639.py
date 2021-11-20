import sys
from collections import deque
data = deque()
tree = {}
while True:
    tmp = sys.stdin.readline().strip()
    if not tmp:
        break
    data.append(int(tmp))

print(data)


def left_tree(pre, root):
    left, right = -1, -1
    if len(pre) == 0:
        return
    parent = pre.popleft()
    if len(pre) == 0:
        return
    if pre[0] < parent:
        left = pre[0]
        if len(pre) >= 1 and pre[1] < root:
            right = pre[1]
    else :
        if pre[0] < root:
            right = pre[0]
    tree[parent] = [left, right]
    if left != -1:
        left_tree(pre, parent)
    if right != -1:
        right_tree(pre, parent)

def right_tree(pre, root):
    left, right = -1, -1
    if len(pre) == 0:
        return
    parent = pre.popleft()
    if len(pre) == 0:
        return
    if pre[0] < parent:
        left = pre[0]
        if len(pre) >= 1 and pre[1] > root:
            right = pre[1]
    else :
        if pre[0] > root:
            right = pre[0]
    tree[parent] = [left, right]
    if left != -1:
        left_tree(pre, parent)
    if right != -1:
        right_tree(pre, parent)


def tree_init(pre):
    left_tree(pre, float("inf"))
    '''
    if pre[0] < root:
        left_tree(pre, root)
    else:
        right_tree(pre, root)

    left, right = -1, -1
    if pre[0] < root:
        left_tree(pre, root)
        left = pre[0]
        if pre[1] > root:
            right = pre[1]
    else :
        right_tree(pre, root)
        right = pre[0]
    '''

tree_init(data)
print(tree)
        
    
