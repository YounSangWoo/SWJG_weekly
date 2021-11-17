#왼쪾으로 레이저 발사, 만나는 첫번째 탑에서만 수신가능, 왼쪽에 노핑보다 큰 수신기가 없으면 수신할 수 없다.
#각 탑의 높이는 서로 다름 
import sys
n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split()))

def razor(stack):
    result = []
    for idx, h in enumerate(stack):
        if idx == 0:
            result.append(0)
        else :
            flag = 0
            temp = stack[:idx]
            temp = temp[::-1]
            for item in temp:
                if item > h:
                    result.append(stack.index(item) + 1)
                    flag = 1
                    break;
            if flag == 0:
                result.append(0)
    return result

print(razor(data))
