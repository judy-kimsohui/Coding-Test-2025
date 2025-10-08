# 계단 오르기!

# 한계단, 두계단씩 오를 수 있음
# 마지막 계단은 반드시 밟아야 함
# 연속된 세 개의 계단을 모두 밟아서는 안된다.

# 각 계단에 쓰여 있는 점수의 합이 최대 구하기 (dp)


N = int(input())
ScoreL = [0]
for _ in range(N):
    ScoreL.append(int(input()))

dp = [0] * (N+1)

dp[1] = ScoreL[1]

if N >= 2:
    dp[2] = ScoreL[2] + ScoreL[1]
if N >= 3:
    dp[3] = ScoreL[3] + max(dp[1], 0 + ScoreL[2]) #dp[start]
if N >= 4:
    for i in range(4, N+1):
        dp[i] = ScoreL[i] + max(dp[i-2], dp[i-3] + ScoreL[i-1])

print(dp[N])
