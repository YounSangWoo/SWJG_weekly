#퀸이 하나 놓이면서 가로줄 세로줄 하나씩 먹고 대각선을 지운다
# 대각선은 

import sys 
data = int(sys.stdin.readline().strip())

class Solution:
    def N_queen(self, N):
        row = [i for i in range(N)]
        col = [i for i in range(N)]
        point = [(i, j) for i in range(N) for j in range(N)]
        rightword = [i for i in range (min(row) - max(col),  max(row) - min(col) + 1)]
        leftword = [i for i in range (min(row) + min(col),  max(row) + max(col) + 1)]
    
        print(row)
        print(col)
        count = 0
        
        # a-b : -7 ~ 7  : 1,  
        # a+b : 0 14 
        # case (0,0) - (0, 7) / (1, 0) (7, 0) 
        

        for a in N:
            for b in N:



        a = 0
        for b in col:
            print(a, b)
            if a - b in rightword:
                if a + b in leftword:
                    if a  
                        row.remove(a)
                        col.remove(b)
                        rightword.remove(a - b)
                        leftword.remove(a + b)
                        print(row)
                        print(col)
                        count += 1
        return count
        
    #첫점을 선택하고
    #순서대로 


    #rcrcrcrcrcrc 
        print(row)
        print(col)
        print(rightword)
        print(leftword)

if __name__=="__main__":
    sol = Solution()
    sol.N_queen(data)

