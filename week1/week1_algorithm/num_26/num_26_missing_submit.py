import sys
import math

data = int(sys.stdin.readline().strip())

class Solution:
    def hanoi_move(self, N, cur, dst):
        if N == 1:
            print(cur, dst)
            return 1
        left_spot = cur ^ dst
        count = self.hanoi_move(N - 1, cur, left_spot)
        count += 1
        print(cur, dst)
        count += self.hanoi_move(N - 1, left_spot, dst)
        return count

if __name__ == "__main__":
    sol = Solution()
    print(pow(2, data) - 1)
    if data <= 20:
        sol.hanoi_move(data, 1, 3)
