import sys
n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(sys.stdin.readline())

class Solution():
    def word_count(self, string):
        string = string.strip()
        div_str = string.split()
        print(div_str)
        count = 0
        for i in div_str:
            count += 1
        return count        

if __name__ == "__main__":
    sol = Solution()
    for string in data:
        print(sol.word_count(string))
