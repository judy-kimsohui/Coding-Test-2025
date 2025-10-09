# 9251_LCS

CS1L = ['0'] + list(input())
CS2L = ['0'] + list(input())

N = len(CS1L)-1
K = len(CS2L)-1

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if CS1L[i] == CS2L[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[N][K])