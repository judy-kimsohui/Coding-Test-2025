# 1516_게임개발
# 건물을 짓는데 걸리는 시간

from collections import defaultdict, deque

N = int(input())


# 각 건물을 짓는데 걸리는 시간
TimeL = [0] * (N+1)

# 각 건물 짓는 규칙 그래프
Graph = defaultdict(list)

# 각 건물의 진입차수 리스트
indegree = [0] * (N+1)

# 건물을 짓는 비용과 선후관계를 동시에 따져야한다
dp = [0] * (N+1)

# 건물 정보 입력
for i in range(1, N+1):
    Input = list(map(int, input().split()))
    TimeL[i] = Input[0]
    for k in Input[1:-1]:        
        Graph[k].append(i)
        indegree[i] += 1

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

for i in range(1, N+1):
    print(dp[i])
        
    