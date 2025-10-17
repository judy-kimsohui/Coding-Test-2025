# 2108_통계학

import math

# N개의 수 (홀수)

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이


N = int(input())
NumberL = []
Sum = 0
for _ in range(N):
    n = int(input())
    NumberL.append(n)
    Sum += n

NumberL.sort()

# 산술평균
print(round(Sum/N))

# 중앙값
print(NumberL[N//2])

# 최빈값
NumberS = set(NumberL)
max = 0
ResultL = []
for n in NumberS:
    Count = NumberL.count(n)
    if max == Count:
        ResultL.append(n)
    elif max < Count:
        ResultL = []
        ResultL.append(n)
        max = Count

ResultL.sort()
if len(ResultL) > 1:
    print(ResultL[1])
else:
    print(ResultL[0])

# 범위
print(NumberL[-1]-NumberL[0])