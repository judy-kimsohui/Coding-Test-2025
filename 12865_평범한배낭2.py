# 아이템 개수, 무게

# 무게, 가치

N, K = map(int, input().split())
ItemL = []
for _ in range(N):
    w, v = map(int, input().split())
    print(ItemL)
    ItemL.append((w, v))

# (인덱스:i개 아이템, 최대 무게) (값:가치)
dp = [0] * (K+1)

for weight, value in ItemL:
    for w in range(K, weight-1, -1):
        dp[w] = max(dp[w], dp[w-weight]+value)
        
print(dp[K])
