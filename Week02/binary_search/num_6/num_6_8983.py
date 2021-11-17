#동물의 수, 사대의수, 사정거리
#:
import sys

M, N, L = list(map(int, sys.stdin.readline().strip().split()))
gun_x = list(map(int, sys.stdin.readline().strip().split()))
point = []
for i in range(N):
    point.append(list(map(int, sys.stdin.readline().strip().split())))

#동물의 위치에서 사대까지의 거리를 생각
#x좌표를 기준으로 정렬을 해야함 
#해당 동물과 사대간의 거리를 알아야겠고 
point.sort(key = lambda axis : axis[0])
gun_x.sort()
#x값 기준으로 정렬 

def animal_search():
    count = 0
    for ani in point:
        start, end = 0, len(gun_x) - 1
        while start < end:
            mid = (start + end) // 2
            if  gun_x[mid] < ani[0]:
                start = mid + 1
            else:
                end = mid
        print(start, end)
        if abs(gun_x[end]-ani[0])+ani[1]<=L or abs(gun_x[end-1]-ani[0])+ani[1]<=L:
            count += 1
    print(count)

        #if abs(ani[0] - gun_x[mid]) + ani[1] <= L or aba(ani[0] - gun_x[mid]) + ani i <= L

            #변하는순간을 찾아야함
            #gun_x가 작을때 
            #gun_x가 커질때 
if __name__ == "__main__":
   animal_search()

#동물의 좌표 x, y, index

