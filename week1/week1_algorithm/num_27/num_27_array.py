#https://junior-datalist.tistory.com/89?category=866196
# abs(queen[i] - queen[row])
import sys
data = int(sys.stdin.readline().strip())

class Solution:
    def search(queen, row):
        n = len(queen)
        count = 0

        if n == row:
            return 1

        for col in range(n):
            queen[row] = col
            if check(queen, row):
                print(count, quuen, row)
                count += search(queen, row + 1)
        return count

    def check(queen, row):
        for i in range(row):
            if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:#대각선 체크 
                return False
        return True 

if __name__ == "__main__":
    sol = Solution()
    sol.search([0] * n, 0)

