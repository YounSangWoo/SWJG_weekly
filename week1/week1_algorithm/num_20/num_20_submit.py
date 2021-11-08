import sys
a,b,v = map(int, sys.stdin.readline().strip().split())

class Solution():
    def snails_dream(self, a, b, v):
        gap = a - b
        last_day = v - b
        k = last_day/gap
        return (int(k) if k == int(k) else int(k) + 1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.snails_dream(a,b,v))

'''
import sys
a,b,v = map(int, sys.stdin.readline().split().strip)

class Solution():
    def snails_dream(self, a, b, v):
        gap = a - b
        last_day = v - b
        k = last_day/gap
        return (int(k) if k == int(k) else int(k) + 1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.snails_dream(a,b,v))
'''
