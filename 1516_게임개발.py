# 1516_게임개발

from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)
indegree = [0] * (N + 1)
timeL = [0] * (N + 1)

# 입력 받기
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    timeL[i] = data[0]  # 건설 시간
    for prev in data[1:-1]:  # -1 전까지가 선행 건물 목록
        graph[prev].append(i)  # prev → i (선행 → 현재)
        indegree[i] += 1

# DP: 각 건물까지 걸린 최소 시간
dp = [0] * (N + 1)
q = deque()

# 진입차수 0인 건물부터 시작
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = timeL[i]

# 위상정렬
while q:
    now = q.popleft()
    for nxt in graph[now]:
        # nxt 건물 완성 시간 = max(기존, now 완료 후 nxt 짓는 시간)
        dp[nxt] = max(dp[nxt], dp[now] + timeL[nxt])
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

# 결과 출력
for i in range(1, N + 1):
    print(dp[i])
