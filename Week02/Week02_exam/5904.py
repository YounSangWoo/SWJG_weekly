#길이가 3, 4, 3, 5, 3, 4, 3, 
#피보나치 수열
import sys
N = int(sys.stdin.readline().strip())

k = 0 
length = 3
while length < N :
    k = k + 1
    length = 2 * length + 3 + k

def Moo(k, length, N):
    if k == 0 :
        if N == 1 :
            return 'm'
        else :
            return 'o'
    length = (length - 3 - k) // 2
    if N <= length:
        return Moo(k - 1, length, N)
    elif N == length + 1 :
        return 'm'
    elif N > length + k + 3 :
        return Moo(k - 1, length, N - length - k - 3)
    else :
        return 'o'
print(Moo(k, length, N))
'''
def Moo(N):
    print("start N", N)
    #n(k+1) = 2 * n(k) + (k+3)

    k = 0
    nums = 3
    while N > nums:
        N = N - nums
        k += 1
        nums = nums + (k + 3)
        print("N, leng_div", N, nums)
    if N > k + 3:
        return Moo(N - (k+3))
    else :
        if N == 1:
            return "m"
        else:
            return "o"

print(Moo(n))
'''


