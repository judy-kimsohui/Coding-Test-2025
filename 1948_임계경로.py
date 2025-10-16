# 1948_임계경로

# 도시 개수 N
# 도로 개수 M
# 도로의 출발 도시 번호, 도착 도시 번호, 도로 걸리는 시간
# 지도를 그리는 사람들의 출발 도시, 도착 도시

# 모든 도시는 출발도시에서 도달이 가능하고, 모든 도시로부터 도착 도시에 도달이 가능하다
from collections import defaultdict, deque

N = int(input())
M = int(input())

Graph = defaultdict(list)
Cost = [[0]*(N+1) for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    a, b, t = map(int, input().split())
    Graph[a].append(b)
    Cost[a][b] = t
    indegree[b] += 1

start, end = map(int, input().split())

# 위상정렬로 최장거리 계산
dp = [0]*(N+1)
back = [[] for _ in range(N+1)]
q = deque([start])

while q:
    now = q.popleft()
    for nxt in Graph[now]:
        indegree[nxt] -= 1
        # 최장 거리 갱신
        if dp[nxt] < dp[now] + Cost[now][nxt]:
            dp[nxt] = dp[now] + Cost[now][nxt]
            back[nxt] = [now]
        elif dp[nxt] == dp[now] + Cost[now][nxt]:
            back[nxt].append(now)
        if indegree[nxt] == 0:
            q.append(nxt)

print(dp[end])  # 최장 거리 출력

# 역추적으로 도로 수 세기
cnt = 0
visited = [False]*(N+1)
q = deque([end])

while q:
    node = q.popleft()
    for prev in back[node]:
        cnt += 1
        if not visited[prev]:
            visited[prev] = True
            q.append(prev)

print(cnt)
