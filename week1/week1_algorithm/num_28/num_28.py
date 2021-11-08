#n은 2의 거듭 제곱 
#4개 set으로 자르고 
#기존의 square가 4배가 된다.
#make_square (4개짜리 1set) x 4set = 16set 
# 
import sys
data = list(map(int, sys.stdin.readline().strip().split()))

class Solution:
    def base_case(self, N, r, c):
        if not r :
            if not c :
                return 0
            else :
                return 1
        else :
            if not c : 
                return 2
            else :
                return 3

    def choose_square(self, N, r, c):
        if N == 1:
            return self.base_case(1, r, c) 
        ret = 0
        cur_pow = pow(2, N - 1)
        if r < cur_pow:
            if c < cur_pow:
                ret += self.choose_square(N - 1, r, c)
            elif c >= cur_pow:
                ret += self.choose_square(N - 1, r, c - cur_pow) + cur_pow * cur_pow
        elif r >= cur_pow:
            if c < cur_pow:
                ret += self.choose_square(N - 1, r - cur_pow, c) + 2 * cur_pow * cur_pow
            elif c >= cur_pow:
                ret += self.choose_square(N - 1, r - cur_pow, c - cur_pow) + 3 * cur_pow * cur_pow
        return ret 
        
if __name__=="__main__":
    sol = Solution()
    print(sol.choose_square(data[0], data[1], data[2]))
#재귀에 대한 분기는 항상 경계점을 주의
