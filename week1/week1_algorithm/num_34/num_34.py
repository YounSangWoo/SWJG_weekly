#순서를 바꿔서 두수의 차의 최댓값을 구하는 함수 
# 9 1 8 2 7 3 4 6 5 

import sys
n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split()))

class Solution:
    def get_max_diff_sum(self, list):
        list.sort()
        even_flag = 0
        if len(list) % 2 == 0:
            even_flag = 1 
        div_point = int(n/2) + even_flag
        smaller = list[0:div_point]
        bigger = list[div_point:-1]
        smaller.reverse()
        bigger.reverse()
        print(smaller)
        print(bigger)
        sum = 0
        for i in range(len(list)):
            print(i, list[i])
            if i == 0:
                sum -= smaller[0]
            elif i % 2 == 0 and i == len(list) - 1:
                sum -= smaller[-1]
            elif i % 2 == 1 and i == len(list) - 1:
                sum += bigger[-1]
            elif i % 2 == 0:
                print("list", sum, i)
                sum -= 2 * smaller[int(i / 2) - 1]
            else:
                sum += 2 * bigger[int(i / 2)]
            print(sum)
        return sum
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.get_max_diff_sum(data))

                

                
                
        #짝수일 경우 반반
        #홀수일 경우 홀수로 시작해야함
