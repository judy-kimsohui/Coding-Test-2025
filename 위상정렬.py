# 위상정렬

from collections import deque, defaultdict

N, K = 5, 4
Graph = defaultdict(list)

# 진입차수
indegree = [0] * (N+1)

edges = [(1,2),(1,3),(3,4),(2,5)]
for a,b in edges:
    Graph[a].append(b)
    
    # 진입차수 기록 - 들어오는 간선
    indegree[b] += 1

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        
        # 진입 차수가 0인 노드 (시작점) 기록
        queue.append(i)

order = []
while queue:
    node = queue.popleft()
    order.append(node)
    
    # 해당 지점에 연결된 부분으로 이동
    for nxt in Graph[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(order)
# 결과: [1, 2, 3, 5, 4] (가능한 순서 중 하나)

# 순서만 찾을 수 있음
# 만약 간선에 비용이 있다면?


# 위상정렬 순서대로 건물을 하나씩 지으면서 각 건물을 짓는 데 걸린 누적 시간을 DP로 기록
# dp[next] = max(dp[next], dp[now] + build_time[next])

