import sys
info = list(map(int, sys.stdin.readline().strip().split()))
data = []
for i in range(info[0]):
    data.append(int(sys.stdin.readline().strip()))
data.sort()

class Solution:
    def check_count(self, N, house, unit, end):
        count = 1
        distance = unit
        while distance < end:
            count += 1
            distance += unit
        if count >= N:
            return 1
        return 0

    def set_unit(self, start, end, N, house):
        save_end = end
        r_count = 1
        while 1:
            if r_count >= N : 
                break;
            unit = int((end - start)/2)
            for spot in house:
                if spot - start > unit:
                    r_count += 1
                    end = spot
                    break;
        
        while self.check_count(N, house, unit, end):
            unit += 1
        return unit - 1
                                  
if __name__ == "__main__":
    sol = Solution()
    print(sol.set_unit(data[0], data[-1], info[1], data))



#why it can be dealayed ?
#because it not come from my think?
