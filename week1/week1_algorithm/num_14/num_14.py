import sys
data = [int(sys.stdin.readline().strip()) for i in range(3)]

class Solution:
    def get_digit_count(self, data):
        ret = data[0] * data[1] * data[2]
        count = [0 for i in range(10)]
        ret = str(ret)
        for i in ret:
            count[int(i)] += 1
        return count
        #ret 은 잘 받았고 for문 돌리면서 count

if __name__ == "__main__":
    sol = Solution()
    num_count = sol.get_digit_count(data)
    for i in num_count:
        print(i)
