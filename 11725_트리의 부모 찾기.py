import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
Graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)

Parent = [0] * (N + 1)

def dfs(node):
    for child in Graph[node]:
        if Parent[child] == 0:   # 아직 부모가 정해지지 않은 경우
            Parent[child] = node
            dfs(child)

dfs(1)

for i in range(2, N + 1):
    print(Parent[i])
