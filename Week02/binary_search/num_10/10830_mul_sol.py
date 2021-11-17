# 행렬 제곱.

import sys

dd
# 행렬 곱셈. n 은 행렬의 크기를 나타내 준다. 
def mul(n, matrix1, matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    
    return result

#2분할. b 가 짝수일때, 홀수일때로 나눠서 접근. '곱셈' 문제와 동일한 방법.
def devide(n, b, matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n, matrix, matrix)
    else:
        # A**8 = A**4 * A**4 = (A ** 2 * A ** 2) * (A ** 2 * A ** 2) 
        # 위의 방식처럼 '분할' 해서 계산하고 재귀를 빠져나오며 차례로 계산한다. 
        temp = devide(n, b//2, matrix)
        if b%2 == 0:
            return mul(n, temp, temp)
        else:
            return mul(n, mul(n,temp, temp), matrix)

n, b = map(int, sys.stdin.readline().split())

matrix_a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = devide(n, b, matrix_a)
for row in result:
    for num in row:
        # 앞에서 모듈라 했는데 왜 또함? b = 1 인경우 mul 연산을 안 수행하기 때문에
        # 따로 모듈라 연산과정이 필요하다. 다른 경우들은 어차피 앞에서 다 하고 와서 모듈라 연산을 해도 값은 동일하다. 
        print(num % 1000, end=' ')
    print()
