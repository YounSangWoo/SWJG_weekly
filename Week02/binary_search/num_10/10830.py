N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
B = bin(B)[2:] #2진법으로 변환

print(B)
