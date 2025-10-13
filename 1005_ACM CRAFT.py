# 1005_ACM CRAFT

from collections import deque, defaultdict

T = int(input())
for _ in range(T):

    # 건물의 개수 N, 건설 규칙 개수 K
    N, K = map(int, input().split())
    
    # 각 건물의 건설 시간
    TimeL = [0] + list(map(int, input().split()))
    
    # 그래프와 "진입차수"
    Graph = defaultdict(list)
    indegree = [0] * (N + 1)
    
    # 건설 규칙 (a → b : a를 지어야 b를 지을 수 있음)
    for _ in range(K):
        a, b = map(int, input().split())
        Graph[a].append(b)
        indegree[b] += 1
    
    # 지어야 하는 목표 건물
    W = int(input())
    
    # DP 배열: 각 건물 완성까지 걸린 최소 시간
    dp = [0] * (N + 1)
    
    # 위상정렬 큐
    queue = deque()
    
    # 선행 건물이 없는 건물부터 시작
    for i in range(1, N + 1):
        if indegree[i] == 0:
            
            # 시작점 추가
            queue.append(i)
            dp[i] = TimeL[i]  # 자기 자신 건설 시간
    
    # 위상정렬 수행
    while queue:
        now = queue.popleft()
        
        for nxt in Graph[now]:
            # 다음 건물 건설에 필요한 시간은,
            # 현재까지의 최대 시간 + 다음 건물 짓는 시간
            dp[nxt] = max(dp[nxt], dp[now] + TimeL[nxt])
            
            # 진입차수 감소
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    
    # 결과: 목표 건물 완성까지 걸린 최소 시간
    print(dp[W])
