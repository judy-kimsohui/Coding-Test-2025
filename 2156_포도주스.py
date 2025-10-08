N = int(input())
GrapeJuiceL = [0]
for _ in range(N):
    GrapeJuiceL.append(int(input()))

dp = [0] * (N+1)

dp[1] = GrapeJuiceL[1]
if N >= 2:
    dp[2] = GrapeJuiceL[2] + GrapeJuiceL[1]
if N >= 3:
    dp[3] = max(dp[2], dp[1] + GrapeJuiceL[3], GrapeJuiceL[2] + GrapeJuiceL[3])

if N >= 4:
    for i in range(4, N+1):
        # i번째 안마심, i번째+i-1번째+dp[i-3], i번째+i-2번째
        dp[i] = max(dp[i-1], dp[i-2] + GrapeJuiceL[i], dp[i-3] + GrapeJuiceL[i-1] + GrapeJuiceL[i])

print(dp[N])