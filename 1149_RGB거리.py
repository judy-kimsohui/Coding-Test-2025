# RGB 거리

# 집이 N개 
# 빨강, 초록, 파랑 중 하나의 색
# 옆 집과 같은색 안됨, 모든 집을 칠하는 최소비용은?
# 각 집을 칠하는 최소비용

N = int(input())
CostL = [[0, 0, 0]]
for _ in range(N):
    R, G, B = map(int, input().split())
    CostL.append([R, G, B])

dp = [[0, 0, 0] for _ in range(N+1)]
dp[1] = CostL[1]


if N >= 2:
    for i in range(2, N+1):
        for k in range(3):
            dp[i][k] = min(dp[i-1][k-1], dp[i-1][k-2]) + CostL[i][k]

print(min(dp[N]))