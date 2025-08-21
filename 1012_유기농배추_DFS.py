import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1

    def dfs(x, y):
        grid[y][x] = 0  # 방문 처리(visited 없이 in-place)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] == 1:
                dfs(nx, ny)

    cnt = 0
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)