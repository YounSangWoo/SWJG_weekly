import sys
n = int(sys.stdin.readline().strip())
data = list([sys.stdin.readline().strip().split() for i in range (n)])

class Solution:
    def babo_sangsoo(self, num_list):
        rev_num1 = ''.join(reversed(str(num_list[0])))
        rev_num2 = ''.join(reversed(str(num_list[1])))
        rev_num1 = int(rev_num1)
        rev_num2 = int(rev_num2)
        ret = []
        ret.append(rev_num1)
        ret.append(rev_num2)
        print(max(ret))

if __name__ == "__main__":
    sol = Solution()
    print(n)
    print(data)
    for case in data:
        sol.babo_sangsoo(case)
    

