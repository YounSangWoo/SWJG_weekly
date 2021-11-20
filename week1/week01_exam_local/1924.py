import sys
data = list(map(int, sys.stdin.readline().strip().split()))#list(int(sys.stdin.readline().strip().split()))

class Solution:
    def month_to_day(self, m):
        sum = 0
        for i in range (1, m):
            if i in [1, 3, 5, 7 , 8, 10, 12]:
                sum += 31
            elif i in [4, 6, 9, 11]:
                sum += 30
            elif i == 2 :
                sum += 28
        return sum 

    def get_week_day(self, day):
        if day % 7 == 0:
            return "MON"
        elif day % 7 == 1:
            return "TUE"
        elif day % 7 == 2:
            return "WED"
        elif day % 7 == 3:
            return "THU"
        elif day % 7 == 4:
            return "FRI"
        elif day % 7 == 5:
            return "SAT"
        else :
            return "SUN"

if __name__ == "__main__":
    sol = Solution()
    day = sol.month_to_day(data[0])
    day += data[1] - 1
    print(sol.get_week_day(day))
    
