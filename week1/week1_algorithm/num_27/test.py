import sys
n = int(sys.stdin.readline().strip())

def search(queen, row):
    num = len(queen)
    count = 0
    if num == row:
        return 1
    for col in range(num):
        queen[row] = col
        if check(queen, row):
            count += search(queen, row + 1)
    return count

def check(queen, row):
    for i in range(row):
        if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:
            return False
    return True 

print(search([0] * n, 0))
