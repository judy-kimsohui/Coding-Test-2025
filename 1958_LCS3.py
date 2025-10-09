# 1958_LCS3

CS1L = list(input())
CS2L = list(input())
CS3L = list(input())

I = len(CS1L)
J = len(CS2L)
K = len(CS3L)

dp = [[[0] * (K+1) for _ in range(J+1)] for _ in range(I+1)]

for i in range(1, I+1):
    for j in range(1, J+1):
        for k in range(1, K+1):
            if CS1L[i-1] == CS2L[j-1] == CS3L[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
            
print(dp[I][J][K])
