#25번
#case 0, other_case 
#5m solve
import sys
data = int(sys.stdin.readline().strip())

#시간 복잡도? 
class Solution:
    def factorial(self, N, mul):
        if N == 0:
            return 1
        elif N == 1:
            return mul
        mul *= N
        return self.factorial(N - 1, mul)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.factorial(data, 1))
    
