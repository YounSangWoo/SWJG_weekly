import sys

sys.setrecursionlimit(10 ** 9)
preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break
#print(preorder)
postorder = []
def pre_to_post(pre, start, end):
    if start > end:
        return
    root = pre[start]
    i = start + 1
    while i <= end and root > pre[i]:
        i += 1
 #   print("idx", start, i, end)
    #print(pre[start])
  #  print("front", pre[start +1:i])
   # print("last", pre[i:end+1])

    pre_to_post(pre, start + 1, i - 1)
    pre_to_post(pre, i, end)
    postorder.append(pre[start])

pre_to_post(preorder, 0, len(preorder) - 1)
for i in postorder:
    print(i)
    
