# 11049_행렬곱셈순서
# 구간 dp
# 작은 구간부터 큰 구간으로 점점 확장해나가!

# 행렬은 곱셈 순서에 따라 연산 수가 달라진다.
# N*M M*K = N M K
# 행렬 N개, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값

N = int(input())
MatrixL = []
for _ in range(N):
    r, c = map(int, input().split())
    MatrixL.append([r, c])

# dp : 곱셈 연산 횟수
# dp[i][j] : i번째 행렬부터 j번째 행렬까지 곱할 때 필요한 최소 연산 횟수
dp = [[0] * N for _ in range(N)]

for length in range(1, N):
    for i in range(N):
        j = i + length
        if j >= N:
            break
        dp[i][j] = float('inf')

        for k in range(i, j):
            cost = (
                dp[i][k]
                + dp[k+1][j]
                + MatrixL[i][0] * MatrixL[k][1] * MatrixL[j][1]
            )
            dp[i][j] = min(dp[i][j], cost)
            
print(dp[0][N-1])