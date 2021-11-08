import sys
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))

class Solution:
    def sort(self, list):
        count = [0 for i in range(10000)]  
        for i in list:
            count[i] += 1
        return count

if __name__  == "__main__":
    sol = Solution()
    count_sort = sol.sort(data)
    for idx, i in enumerate(count_sort):
        while (i):
            print(idx)
            i -= 1

