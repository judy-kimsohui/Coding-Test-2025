# 정수 삼각형!

N = int(input())
NumberL = [[0]]
for i in range(N):
    L = list(map(int, input().split()))
    NumberL.append(L)

for i in range(N-1, 0, -1):    
    for k in range(0, i):
        NumberL[i][k] += max(NumberL[i+1][k], NumberL[i+1][k+1])

print(NumberL[1][0])