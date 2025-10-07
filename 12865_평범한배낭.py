# 아이템 개수, 무게

# 무게, 가치

N, K = map(int, input().split())
ItemL = []
for _ in range(N):
    w, v = map(int, input().split())
    print(ItemL)
    ItemL.append((w, v))

# (인덱스:i개 아이템, 최대 무게) (값:가치)
dp = [[0] * (K+1) for _ in range(N+1)]
print(dp)
for i in range(1, N+1):

    # 확인할 아이템의 무게, 가치
    weight, value = ItemL[i-1]

    # 이 아이템을 넣을것인가?
    for w in range(1, K+1):
        
        # 넣을 수 없다 (dp의 초반 부분일 때)
        if weight > w:
            dp[i][w] = dp[i-1][w]
        # 넣을 수 있다
        else:                    
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)

# 결과    
print(dp[N][K])