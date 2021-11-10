import sys
n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split()))

class Solution:
    def even_case(self, list):
        bigger = list[0:int(n/2)]
        smaller = list[int(n/2):]
        print(bigger)
        print(smaller)
        sum = 0
        s_idx = 0
        b_idx = 0
        for idx in range(len(list)):
            if idx % 2 == 0 : 
                if idx == 0:
                    sum -= smaller[s_idx]
                    s_idx += 1
                else :
                    sum -= 2 * smaller[s_idx]
                    s_idx += 1
            else:
                if idx == len(list) - 1:
                    sum += bigger[b_idx]
                    b_idx += 1
                else :
                    sum += 2 * bigger[b_idx]
                    b_idx += 1
            print(sum)
        return sum 

    def odd_case(self, list):
        bigger = list[0:int(n/2)]
        smaller = list[int(n/2):]
        sum = 0
        for idx in range(len(list)):
            s_idx = 0
            b_idx = 0
            if idx % 2 == 0 or idx == len(list) - 1:
                if idx == 1:
                    sum -= smaller[s_idx]
                    s_idx += 1
                else :
                    sum -= 2 * smaller[s_idx]
                    s_idx += 1
            else :
                sum += 2 * bigger[b_idx]
                b_idx += 1
            print(sum)
        return sum

    def get_max_diff_sum(self, list):
        print(list)
        sort_list = sorted(list)
        print(sort_list)
        sort_list.reverse()

        print(sort_list)
        if len(sort_list) % 2 == 0:
            return self.even_case(sort_list)
        else: 
            return self.odd_case(sort_list)
'''
        div_point = int(n/2) + even_flag
        smaller = list[0:div_point]
        bigger = list[div_point:-1]
        smaller.reverse()
        bigger.reverse()
        sum = 0
        for i in range(len(list)):
            print("chack", list, len(list))
            if i == 0:
                print(i)
                sum -= smaller[0]
            elif i % 2 == 0 and i == len(list) - 1:
                print(i)
                sum -= smaller[-1]
            elif i % 2 == 1 and i == len(list) - 1:
                print(i)
                sum += bigger[-1]
            elif i % 2 == 0:
                print(i)
                sum -= 2 * smaller[int(i / 2)]
            else:
                print(i)
                sum += 2 * bigger[int(i / 2) - even_flag]
        return sum
''' 
if __name__ == "__main__":
    sol = Solution()
    print(sol.get_max_diff_sum(data))
