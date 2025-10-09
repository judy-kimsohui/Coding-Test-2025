# 9252_LCS2

CS1L = list(input())
CS2L = list(input())

N = len(CS1L)
K = len(CS2L)

dp = [[0] * (K+1) for _ in range(N+1)]
wordL = [[''] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if CS1L[i-1] == CS2L[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            wordL[i][j] = wordL[i-1][j-1] + CS1L[i-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if len(wordL[i-1][j]) == dp[i][j]:
                wordL[i][j] = wordL[i-1][j]
            else:
                wordL[i][j] = wordL[i][j-1]
            
print(dp[N][K])
print(wordL[N][K])
