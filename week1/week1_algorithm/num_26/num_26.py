# 2 개 일때까지만 생각 
# ret = count
# 재귀에도 self

import sys
data = int(sys.stdin.readline().strip())

class Solution:
    def hanoi_move(self, N, cur, dst, list):
        if N == 1:
            list.append([cur, dst])
            return 1
        left_spot = cur ^ dst
        count = self.hanoi_move(N - 1, cur, left_spot, list) #1, 2 : 1, 2  

        list.append([cur, dst])
        count += 1 # 제일 큰판  
        count += self.hanoi_move(N - 1, left_spot, dst, list)
        return count

if __name__ == "__main__":
    sol = Solution()
    list = []
    print(sol.hanoi_move(data, 1, 3, list))
    for item in list:
        print(item[0], item[1])


    last 
#a 1 -> 1                                                   -> 2^1 -1
#b 2 -> 1  + 2 * (a)                                        -> 1 + 2 * (2^1 -1) = 
#c 3 -> 1  + 2 * (b) = 1 + 2 * (1 + 2 * (a))
#d 4 -> 1  + 2 * (c) = 1 + 2 * (c) = 1 + 2 * (1 + 2 * (b))

(1) + (1 + 2 * 1) + (1 + 2 * (1 + 2 * 1))
(2^1 - 1) 

2 * (2^n-1 -1) = (2^n - 2) + 1   


2^n + 1 = 2 ^ n

1 + 2
1 + n(2)
1 + 2(1 + former )
