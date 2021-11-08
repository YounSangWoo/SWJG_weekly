import sys

data = [sys.stdin.readline().strip() for i in range(6)]

class Solution:
    def ascii_code(self, input):
        if type(input) == int:
            return chr(input)
        else :
            return ord(input)

if __name__ == "__main__":
    sol = Solution()
    for input in data:
        print(sol.ascii_code(input))
