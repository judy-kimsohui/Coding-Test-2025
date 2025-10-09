# 15483_최소편집

CS1L = list(input())
CS2L = list(input())

# A에 연산을 최소 횟수로 수행해 B로 만드는 문제를 "최소 편집" 문제
# 삽입: A의 한 위치에 문자 하나를 삽입한다.
# 삭제: A의 문자 하나를 삭제한다.

# 교체: A의 문자 하나를 다른 문자로 교체한다. (중요!!)

I = len(CS1L)
J = len(CS2L)

dp = [[0] * (J+1) for _ in range(I+1)]
# dp[i][j] = A의 앞 i개를 B의 앞 j개로 바꾸는 최소 연산 횟수

# 초기화 (빈 문자열에서 만드는 경우)
for i in range(I + 1):
    dp[i][0] = i
for j in range(J + 1):
    dp[0][j] = j

for i in range(1, I+1):
    for j in range(1, J+1):
        if CS1L[i-1] == CS2L[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(
                dp[i - 1][j],     # 삭제 - A의 마지막 문자를 제거하고 비교
                dp[i][j - 1],     # 삽입 - B의 마지막 문자를 A에 삽입
                dp[i - 1][j - 1]  # 교체 - A의 마지막 문자를 B의 마지막으로 교체
            ) + 1

print(dp[I][J])
