# 시간이 O(N)이라 백준 기준으로 충분히 통과된다

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
Graph = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)

Parent = [0] * (N + 1)

def dfs(node, parent):
    Parent[node] = parent
    for child in Graph[node]:
        if child != parent:
            dfs(child, node)

dfs(1, 0)

for i in range(2, N + 1):
    print(Parent[i])
