#단어를 정렬, 길이가 짧은 것부터, 길이가 같으면 사전 순으로 
#길이가 짧다 -> len으로
#사전 순 정렬 -> 리스트 

import sys
n = int(sys.stdin.readline().strip())
data = []
for i in range (n):
    data.append(sys.stdin.readline().strip())

class Solution:
    def arr_str(self, list):
        dict = {}
        for word in list:
            if dict.get(len(word)):
                if word not in dict[len(word)]:
                    dict[len(word)].append(word)
            else :
                dict[len(word)] = [word]
        return dict

if __name__ == "__main__":
    sol = Solution()
    dict = sorted(sol.arr_str(data).items())
    for list in dict:
        list[1].sort()
        for i in list[1]:
            print(i)
