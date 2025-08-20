# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# - 그래프 문제

from collections import defaultdict

C = int(input()) # 컴퓨터 수
N = int(input()) # 네트워크 쌍 수
graph = defaultdict(list)

for _ in range(N):
    a, b = map(int, input().split())
    # 양방향 그래프
    graph[a].append(b)
    graph[b].append(a)
    
# DFS로 그래프의 노드 탐색
visitedL = [False] * (C + 1)
infected = 0

def dfs(node):
    global infected
    visitedL[node] = True
    for n in graph[node]:
        if not visitedL[n]:
            infected += 1
            dfs(n)
            
dfs(1)
print(infected)