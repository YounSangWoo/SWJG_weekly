import sys
import math

A, B, C = list(map(int, sys.stdin.readline().strip().split()))

def cnt_overC(left, C):
    count = 1
    while (left <= C):
        left *= left
        count += 1
    return count

def div_within_div(A, B, C):
    num = A % C
    if num <= 1 or B  <= 1:
        return num
    if C == 1:
        return 0
    c = cnt_overC(num, C)
    b = B // c
    b_c = B % c
    #print("n, c, b, b_c", num, c, b, b_c)
    last_div = div_within_div(pow(num, c), b, C) * (pow(num, b_c) % C)
    return last_div % C

print(div_within_div(A, B, C))
