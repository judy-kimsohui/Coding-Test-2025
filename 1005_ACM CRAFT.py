# 1005_ACMCraft
# 건물을 짓는데 걸리는 시간

from collections import defaultdict, deque

T = int(input())

# 테스트 케이스 T
for t in range(T):
    
    # 건물의 개수 N, 규칙 K
    N, K = map(int, input().split())
    
    # 각 건물을 짓는데 걸리는 시간
    # 인덱스는 1부터 시작
    TimeL = [0] + list(map(int, input().split()))
    
    # 각 건물 짓는 규칙 그래프
    Graph = defaultdict(list)
    
    # 각 건물의 진입차수 리스트
    indegree = [0] * (N+1)
    
    # 건물을 짓는 비용과 선후관계를 동시에 따져야한다
    dp = [0] * (N+1)
    
    # 건물 짓는 규칙
    for _ in range(K):
        a, b = map(int, input().split())
        Graph[a].append(b)
        indegree[b] += 1
    
    # 마지막에 지어야 하는 목표 건물 W
    W = int(input())
    
    # 먼저 짓는 건물들
    Q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            Q.append(i)
            dp[i] = TimeL[i]
    
    # 선후관계 조사 (건물번호)
    while Q:
        node = Q.popleft()
        for n in Graph[node]:
            indegree[n] -= 1
            dp[n] = max(dp[n], dp[node] + TimeL[n])
            if indegree[n] == 0:
                Q.append(n)
    
    print(dp[W])
        
        
    