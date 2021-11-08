'''
높이가 V미터인 나무막대 
+A -B : 실제로는 낮에 V - A 일 경우 도착
+A - B 반복 돌리고, if 문으로 도착 체크 
'''
import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

class Solution():
    def snails_dream(self, list):
        gap = list[0] - list[1]
        last_day = list[2] - list[0]
        if (last_day / gap) < 1 :
            return 2
        return int(last_day / gap) + 1

'''
        while (1):
            cur += list[0]
            if cur >= list[2]:
                day += 1
                return(day)
            cur -= list[1]
            if list[0] is 100:
                print(day, cur)
            day += 1
        return day
'''
if __name__ == "__main__":
    sol = Solution()
    for list in data:
        print(sol.snails_dream(list))

        
        


