# 오름차순 정렬
#선택 정렬 :  
#리스트를 나누는 방식도 의미가 있나 ? 

import sys 
n = int(sys.stdin.readline().strip())
data = []
for i in range (n):
    data.append(int(sys.stdin.readline().strip()))

class Solution:
    def merge_sort(self, arr): # 이런식으로 함수내부에 함수 쓰는게 가능한가 ?
        def sort(low, high):
            if high - low < 2:
                return
            mid = (low + high) // 2 
            sort(low, mid)
            sort(mid, high)
            merge(low, mid, high)

        def merge(low, mid, high):
            temp = []
            l, h = low, mid 
            while l < mid and h < high:
                if arr[l] < arr[h]:
                    temp.append(arr[l])
                    l += 1
                else:
                    temp.append(arr[h])
                    h += 1

            while l < mid:
                temp.append(arr[l])
                l += 1
            while h < high:
                temp.append(arr[h])
                h += 1
            for i in range(low, high):
                arr[i] = temp[i - low]
        return sort(0, len(arr))
        
if __name__== "__main__":
    sol = Solution()
    sol.merge_sort(data)
    for num in data:
        print(num)



