#주어진건 개수이고, 거리는 제한이 없다, 
#기본적으로 중앙값은 리스트의 값이 아니라 실제 값이어야함
#중앙값에서 포인터를 양쪽으로 보내서 가까운 값을 찾아야함 
#이제 반대 쪽에서 중앙 인근의 값을 찾아야함-> 재귀
#그 뒤에 그 전의 선택받지 못한 길이와 현재의 선택받지 못한 길이를 비교해야함
'''
    def set_near_mid(self, start, end, N, house): #start : 검색 가능 시작점, end : 검색 가능 끝점, 남은 설치 대수 
        if N == 0:
            return
        if (start + end) % 2 = 1:
            
        left = int((start + end)/2)
        right = left
        #compare가 필요함 
        for i in range (int((start + end)/2):
            if right in house:
                house.remove(right)
                

                self.set_name_mid(start, left, N - 1, house)
                #하나 찾고 다음 search 그럼 두개중 큰 곳으로 가야함 
                #
            if left in house:
                house.remove(left)
                self.set_name_mid(right, end, N - 1, house)
            right, left += 1

        print (left, right)
'''
    #거리만을 구하는 방법으로 

import sys
info = list(map(int, sys.stdin.readline().strip().split()))
data = []
for i in range(info[0]):
    data.append(int(sys.stdin.readline().strip()))
data.sort()

class Solution:
    def get_mid(self, start, end, N, house):
        count = 1
        save_end = end
        min = end - start
        install_idx = [0]
        if N == 0:
            return
        while count < N:
            mid = int((end - start) / 2) + 1
            for i in range(mid, end + 1):
                if i in house:
                    min = i - start
                    idx = house.index(i)
                    end = house[idx]
                    install_idx.append(idx)
                    count += 1 
                    break;
        #count = N 일때 루프 돌리는 목적?)
        #end를 초기화 하면서 가장 균일하게 분절 -> min 값은 마지막 mid보다 큰 값이지, 실제 min값은 아님 .
        install_idx.sort()
        s_list = [house[s_index] for s_index in install_idx]
        s_list.append(save_end)
        for i in range(0, len(s_list) - 1):
            gap = s_list[i + 1] - s_list[i]
            if min > gap:
                min = gap
        return min

    def check_count(self, N, house, unit):
        count = 1
        distance = unit
        while distance < unit:
            count += 1
            distance += unit
        if count >= N:
            return 1
        return 0
            
    def set_unit(self, start, end, N, house):
        flag = 0
        #break는 루프 하나를 탈출할 때 쓴다. 
        while 1:
            count = 1
            unit = int((end - start)/2) + 1
            #단위를 정함 점점 작아진다. 
            for spot in house:
                if spot > unit: 
                    self.check_count(N, house, unit)
                    min_d = spot - start
                    count += 1
                    #필요한것 
                    #count가 몇개인지 카운트가 뭐지? 전체 개수 count 개수만 리턴 받으면 된다. 
                    #count가 어떻게 되는건지도 ..  
                    if self.check_count(N, house, min_d):
                        while self.check_count(N, house, min_d):
                            unit += 1
                        unit -= 1
                        return unit
                    else :
                        end = spot
                        flag = 1
                        break;
            if flag == 1: 
                break; 
                        #end땡겨야함
                        #count 리셋 해야되나 ? 
                        #unit 초기화는 알아서 될거고 


#지금 이거 내 함수가 아니야
#셀프 카운트로 세서 된다고 쳐 그다음에 그 앞에 꺼 어떻게 받아올꺼야?
#아닐 경우 ? conitunue 
                        
                        
                        
                    
            #내가 생각하는 방식이랑 아예 다름 
#루프를 돌리면서 반으로 쪼개감
#min_ddd는 distance를 update
#
                            

if __name__ == "__main__":
    sol = Solution()
    print(data)
    print(sol.set_unit(data[0], data[-1], info[1], data))
