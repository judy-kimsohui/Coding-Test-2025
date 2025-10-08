# 10942_팰린드롬

import sys
input = sys.stdin.readline
write = sys.stdout.write

# 팰린드롬 놀이
# 거꾸로 읽어도 제대로 읽는 것과 같은 문장이나 낱말, 숫자, 문자열

# 자연수 N개, 질문을 M번
# 두 정수 S, E
# S~E가 팰린드롬을 이루는가? (맞다, 아니다) 대답

N = int(input())
NumberL = [0] + list(map(int, input().split()))
M = int(input())
Query = [list(map(int, input().split())) for _ in range(M)]

# 구간 dp
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][i] = 1

for length in range(2, N+1):
    # +2 주의
    for s in range(1, N + 1):
        e = s + length-1
        if e > N:
            break  # e가 범위를 넘으면 더 볼 필요 없음
        if NumberL[s] == NumberL[e]:
            # 길이가 2인 경우 따로 처리해줘야함
            if length == 2 or dp[s+1][e-1] == 1:
                dp[s][e] = 1

result = []
for s, e in Query:
    result.append(str(dp[s][e]) + "\n")

write("".join(result))