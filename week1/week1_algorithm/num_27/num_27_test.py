import sys
n = int(sys.stdin.readline().strip())

class Solution:
    def search(self, queen, row):
        n = len(queen)
        count = 0
        if n == row:
            return 1
        for col in range(n):
            queen[row] = col
            if self.check(queen, row):
                count += self.search(queen, row + 1)
        return count

    def check(self, queen, row):
        for i in range(row):
            if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:
                return False
        return True 

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([0] * n, 0))
