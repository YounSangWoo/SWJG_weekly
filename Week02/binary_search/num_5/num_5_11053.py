#증가하는 부분 수열의 의미?
#둘째 줄에 수열 A를 이루고 있는 Aj
#그냥 필요없는거 버리면 될것 같은데 시간복잡도가 문제네
#이분탐색으로 이걸 어떻게 줄이지?
#dp로 각각의 루트를 전부 카운트하네 


import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

def get_part_array(n, data):
    array = [1] * n
    for i in range(n):
        for j in range(i):
            print("check", i, j)
            if data[j] < data[i]:
                array[i] = max(array[i], array[j]+1)
                print(data[i], array[i], array[j])
                print(array)
    return array

if __name__ == "__main__":
    print(max(get_part_array(n, data)))
