# 1로 만들기!

# X가 3으로 나누어떨어지면 3으로 나누고, 2로 나누어떨어지면 2로 나눈다, 1을 뺀다
# 연산을 사용하는 최소값을 구하라

N = int(input())

count = 0

dp = [0] * (N+1)
dp[1] = 0

if N >= 2:
    dp[2] = 1
if N >= 3:
    dp[3] = 1
if N >= 4:
    dp[4] = 2

if N >= 5:
    for i in range(5, N+1):
        if i % 3 == 0 and i % 2 == 0:
            dp[i] = min(dp[i-1], dp[int(i/3)], dp[int(i/2)]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i-1], dp[int(i/3)]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i-1], dp[int(i/2)]) + 1
        else:
            dp[i] = dp[i-1] + 1    

print(dp[N])