# 12015_가장 긴 증가하는 부분 수열 2
# N = int(input())
# Array = list(map(int, input().split()))

# dp = [[0] * (N) for _ in range(N)]
# numP = [[0] * (N) for _ in range(N)]
# # dp[i][j] : i 부터 j까지 증가하는 부분 수열 정보

# for i, num in enumerate(Array):
#     dp[i][i] = num
#     numP[i][i] = 1

# for length in range(2, N+1):
#     for i in range(N):
#         j = i + length -1
#         if j > N-1:
#             break
#         if dp[i][j-1] < Array[j]:
#             dp[i][j] = Array[j]
#             numP[i][j] = numP[i][j-1] + 1
#         else:
#             dp[i][j] = dp[i][j-1]
#             numP[i][j] = numP[i][j-1]

# print(numP[0][N-1])
            

# DP
# ------------------------
# N = int(input())
# A = list(map(int, input().split()))

# dp = [1] * N  # dp[i] = A[i]를 마지막 원소로 하는 LIS의 길이

# for i in range(N):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))



# 이분탐색
# ------------------------
import bisect

N = int(input())
A = list(map(int, input().split()))

dp = []  # 각 길이별 증가 부분 수열의 마지막 값

for num in A:
    pos = bisect.bisect_left(dp, num)
    # 끝값이라면 추가하기
    if pos == len(dp):
        dp.append(num)
    else:
        # num이 들어갈 위치에 교체 → 더 작은 끝값 유지
        dp[pos] = num

print(len(dp))

