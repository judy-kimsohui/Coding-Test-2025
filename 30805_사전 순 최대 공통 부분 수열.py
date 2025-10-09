# 30805_사전 순 최대 공통 부분 수열

# 해당 수열의 원소들이 다른 수열 내에서 순서대로 등장

I = int(input())
CS1L = list(map(int, input().split()))
J = int(input())
CS2L = list(map(int, input().split()))

# A와 B의 공통 부분 수열 중 사전 순으로 가장 나중인 수열의 크기 K를 출력

# 두 수열 중 첫 번째 수가 큰 쪽은 사전 순으로 나중입니다.
# 두 수열의 첫 번째 수가 같다면, 첫 번째 수를 빼고 두 수열을 다시 비교했을 때 사전 순으로 나중인 쪽이 사전 순으로 나중입니다.
# 길이가 0인 수열과 다른 수열을 비교하면, 다른 수열이 사전 순으로 나중입니다.
            
dp = [[0] * (J+1) for _ in range(I+1)]
# dp[i][j] = A의 앞 i개를 B의 앞 j개로 바꾸는 최소 연산 횟수

numberL = [[''] * (J+1) for _ in range(I+1)]

for i in range(1, I+1):
    for j in range(1, J+1):
        if CS1L[i-1] == CS2L[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            numberL[i][j] = numberL[i-1][j-1] + str(CS1L[i-1])                
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if numberL[i-1][j] > numberL[i][j-1]:
                numberL[i][j] = numberL[i-1][j]
            else:
                numberL[i][j] = numberL[i][j-1]

resultL = list(numberL[I][J])
N = len(resultL)
answerL = resultL[:]
for i, num in enumerate(resultL):    
    if i < N-1 and num < resultL[i+1]:
        print(i)
        answerL[i] = "-"
    
print(len(answerL))
print(" ".join(answerL).strip("- "))


