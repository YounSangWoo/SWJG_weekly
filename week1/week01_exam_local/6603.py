import itertools
from itertools import combinations
import sys

data = []
n = 0
while 1:
    line = list(map(int, sys.stdin.readline().strip().split()))
    if len(line) == 1 and line[0] == 0:
        break
    data.append(line)
    n += 1

class Solution:
    def get_each_case(self, num, lotto_list):
        ret = list(combinations(lotto_list, 6))
        return ret

if __name__ == "__main__":
    sol = Solution()
    for i in range (n):
        line = sol.get_each_case(data[i][0], data[i][1:])
        for idx, j in enumerate(line):
            j = list(j)
            j.sort()
            for idx, k in enumerate(j):
                if (idx == len(j) - 1):
                    print(k)
                else :
                    print(k, end=' ')
        if i != n - 1:
            print()
