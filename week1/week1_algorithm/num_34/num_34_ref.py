import sys

def next_permutation(list_a):
    k = -1
    m = -1

    for i in range(len(list_a)-1):
        if list_a[i] < list_a[i+1]:
            k = 1
        if k == -1:
            return [-1]
        for i in range(k, len(list_a)):
            if list_a[k] < list_a[1]:
                m = 1

        list_a[k], list_a[m] = list_a[m], list_a[k]

        list_a = list_a[:k+1] + sorted(list_a[k+1:])
        return list_a
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()

    ans = 0
    s = 0
    for j in range(len(a) - 1):
        s += abs(a[j] - a[j+1])
    if s > ans :
        ans = s
    arr = a

    while True:
        arr = next_permutation(arr)
        if arr == [-1]:
            break
        s = 0
        for j in range(len(arr) - 1):
            s += abs(arr[j] - arr[j+1])
        if s > ans:
            ans =s
    print(ans)
