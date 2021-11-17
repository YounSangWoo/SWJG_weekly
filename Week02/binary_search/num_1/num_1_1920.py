import sys

n = int(sys.stdin.readline())
data1 = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
data2 = list(map(int, sys.stdin.readline().strip().split()))

class Solution:
    def binary(self, l, N, start, end):
        if start > end:
            return 0
        m = (start+end)//2
        if l == N[m]:
            return 1
        elif l < N[m]:
            return self.binary(l, N, start, m-1)
        else:
            return self.binary(l, N, m+1, end)

if __name__ == "__main__":
    sol = Solution()
    data1.sort()
    for item in data2:
        start = 0
        end = len(data1) - 1
        print(sol.binary(item,data1,start,end))
