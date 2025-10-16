# 2231_분해합

Number = int(input())

start = max(0, Number - 9 * len(str(Number)))
result = 0

for n in range(start, Number):
    sumN = 0
    tempN = n
    while tempN > 0:
        sumN += tempN % 10
        tempN //= 10
    if n + sumN == Number:
        result = n
        break

print(result)
