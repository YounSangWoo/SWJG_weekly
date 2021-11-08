#그냥 입출력 방식 백준 case랑 똑같이 만드는게 효율적일듯 
# 한수 : 어떤 양의 정수 X와 각 자리가 등차수열을 이룬다.
# under 100 : n = n개 default
# n 에서 딱 끊엇어 1의자리, 10의자리, 100의 자리 
# incre case decre case
# 100의 자리 
# 예를들어 145, 순서대로 체크하면 되 
# 169 
# 258 
# upcase downcase 
# num, 5 7
import sys
num = int(sys.stdin.readline().strip())

class Solution():
    def get_each_num(self, num):
        ret = []
        ret.append(int(num/100))
        num = (num % 100)
        ret.append(int(num/10))
        num = (num % 10)
        ret.append((num))
        return ret

    def count_case(self, num):
        if num == 0:
            return 0
        count = 0
        for i in range(100, num + 1):
            digit = self.get_each_num(i)
            if digit[0] - digit[1] == digit[1] - digit[2]:
                count += 1
        return count
        
    def count_han_soo(self, num):
        if num < 100 :
            return num
        else:
            return 99 + self.count_case(num)

if __name__ == "__main__":
    sol = Solution()
    print(sol.count_han_soo(num))
