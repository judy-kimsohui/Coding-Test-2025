# 2252_줄세우기

from collections import defaultdict, deque

Student, M = map(int, input().split())

Graph = defaultdict(list)
indegree = [0] * (Student + 1)  # 각 노드의 진입 차수

for _ in range(M):
    a, b = map(int, input().split())
    Graph[a].append(b)
    indegree[b] += 1

# 비용에 대한 내용이 없으므로, 선후관계만 따지면 된다.
result = []
Q = deque()

# 먼저 설 수 있는 학생들
# 진입 차수가 0인 노드를 큐에 넣기
for i in range(1, Student + 1):
    if indegree[i] == 0:
        Q.append(i)

# 학생들 다음으로 선후관계 조사
while Q:
    now = Q.popleft()
    result.append(now)

    # 현재 노드와 연결된 노드들의 진입차수 감소
    for nxt in Graph[now]:
        indegree[nxt] -= 1
        
        # 만약 더이상 들어오는게 없다면 (사전 확인 끝남)
        if indegree[nxt] == 0:
            
            # 큐에 넣기
            Q.append(nxt)

print(*result)