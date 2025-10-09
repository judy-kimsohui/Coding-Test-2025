# 11066_파일합치기
# 구간 dp
# 작은 구간부터 큰 구간으로 점점 확장해나가!

T = int(input())
for _ in range(T):
    N = int(input())
    BookL = list(map(int, input().split()))

    # dp[i][j] : i번째 책부터 j번째 책까지 합칠때의 비용
    dp = [[0] * N for _ in range(N)]

    prefix = [0] * (N+1)
    for idx in range(1, N+1):
        prefix[idx] = prefix[idx-1] + BookL[idx-1]
    
    for length in range(1, N+1):
        for i in range(N):
            j = i + length
            if j >= N:
                break

            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k+1][j]
                    + (prefix[j+1] - prefix[i])
                )
                dp[i][j] = min(dp[i][j], cost)

    print(dp[0][N-1])