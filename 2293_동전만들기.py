# 동전1
# n가지 종류 동전을 적당히 사용해서 가치가 k 되게 하고싶다
# 경우의 수 구하기

n, k = map(int, input().split())
DongL = []
for _ in range(n):
    DongL.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for dong in DongL:        
    for i in range(dong, k+1):
        dp[i] += dp[i-dong]
    
print(dp[k])