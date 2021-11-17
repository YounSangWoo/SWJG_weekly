#넣고 닫는건 가능해
#0, 1 만나서 하나의원 -> count + 1 하고 
#아직 진행중인 원이 있을때 2, r을 넣고 r들을 합쳐서 닫히는원의 x좌표 차이가 같다면 + 1 // 어차피 밖에는 영향을 못 미침


#stack에 반지름순, x좌표 순대로 
#좌표를 sorting하고 
#들어온 x,r을-> left와 x좌표, right와 x좌표로 나눌 수 있음 

import sys
n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x, r = list(map(int, sys.stdin.readline().split()))
    points.append([0, x-r])
    points.append([1, x+r])
points.sort(key=lambda x:(x[1], -x[0])) #동일한 좌표일 경우 right가 먼저와야됨 (동시에 원이 열리고 닫힌다면 닫히는걸 처리해주고 뒤쪽 원을 봐야함

print(points)

def count_space(points):
    stack = []
    count = 1 
    for item in points:
        if item[0] == 0:
            stack.append(item)
        elif item[0] == 1: #원 하나가 닫힘
            r_sum = 0 #내부 원들의 반지름의 합 = 큰원의 반지름이면 +1
            while stack[-1][0] == 2: #내부원의 존재 확인
                tmp = stack.pop() #내부 원이 있을 경우 pop
                r_sum += tmp[1] #내부원 반지름의 합에 현재 내부원의 반지름을a add 
            r_cur = (item[1] - stack[-1][1])//2 #비교를 위해 현재 큰원의 반지름 길이 
            if r_sum == r_cur: #같을 경우 영역 + 1
                count += 1
            stack.pop() #원이 닫혔으므로 원의 left를 pop
            stack.append([2, r_cur]) # 이후 현재원이 더 큰원의 내부가 될 경우 를 대비해서 현재원의 반지름 리스트 key : 2
            count += 1
        print(stack, count)
    print(count)

count_space(points)
