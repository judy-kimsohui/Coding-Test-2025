# 5582_공통 부분 문자열

CS1L = list(input())
CS2L = list(input())

N = len(CS1L)
K = len(CS2L)

result = 0
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if CS1L[i-1] == CS2L[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(result, dp[i][j])
        else:
            dp[i][j] = 0
            
print(result)