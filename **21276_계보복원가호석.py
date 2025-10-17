# 21276_계보복원가호석

from collections import defaultdict, deque

N = int(input())
names = input().split()
names.sort()  # 사전순 출력용

M = int(input())
graph = defaultdict(list)
indegree = {name: 0 for name in names}  # 부모 수
children = {name: [] for name in names}  # 직속 자식

for _ in range(M):
    X, Y = input().split()  # X의 조상 중에 Y가 있다 → Y → X
    graph[Y].append(X)
    indegree[X] += 1

# 위상정렬로 “직속 부모”만 판별
q = deque()
for name in names:
    if indegree[name] == 0:
        q.append(name)

while q:
    now = q.popleft()
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            # now가 nxt의 “직속 부모”
            children[now].append(nxt)
            q.append(nxt)

# 시조 출력
roots = [name for name in names if indegree[name] == 0]
print(len(roots))
print(*roots)

# 각 사람별 자식 출력
for name in names:
    child_list = sorted(children[name])
    print(name, len(child_list), *child_list)


