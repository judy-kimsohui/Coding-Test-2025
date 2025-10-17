# 1766_문제집
# 위상정렬 + 우선순위 큐(min-heap)

# 1번부터 N번까지 총 N개의 문제
# 1번이 가장 쉽고, N번이 가장 어려운 문제

# N개의 문제는 모두 풀어야 한다.
# 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
# 가능하면 쉬운 문제부터 풀어야 한다.

import heapq
from collections import defaultdict

N, M = map(int, input().split())
Graph = defaultdict(list)
indegree = [0] * (N + 1)

# 간선 입력
for _ in range(M):
    a, b = map(int, input().split())
    Graph[a].append(b)
    indegree[b] += 1

# 최소 힙(숫자 작은 문제부터 꺼냄)
heap = []

# 진입 차수 0인 문제를 전부 힙에 추가
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    now = heapq.heappop(heap)  # 가장 번호 작은 문제
    result.append(now)
    for nxt in Graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(heap, nxt)

print(*result)

