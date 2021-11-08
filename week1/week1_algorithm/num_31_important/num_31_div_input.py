#data input change 
import memory_usage
import sys
n = int(sys.stdin.readline().strip())
count = [0 for i in range(10001)]
for i in range (n):
    temp_num = int(sys.stdin.readline().strip())
    count[temp_num] += 1
for idx, i in enumerate(count):
    while (i):
        i-=1
print(memory_usage.memory_usage('mem'))

#data 를 리스트의 형태로 저장하지 않는다.
#input을 list로 저장하지 말고 그때 그때 저장 

#8MB = 1024 * 1024 

