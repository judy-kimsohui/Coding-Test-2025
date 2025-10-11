# 프로그래머스_2023_미로탈출

import sys
sys.setrecursionlimit(10000)

def solution(n, m, x, y, r, c, k):
    # 1-based → 0-based
    x, y, r, c = x - 1, y - 1, r - 1, c - 1

    # 방향 (사전순)
    dirs = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    # 최소 거리 계산
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 != 0:
        return "impossible"

    result = None
    path = []

    def dfs(cx, cy, remain):
        nonlocal result
        # 이미 찾았으면 바로 중단
        if result is not None:
            return True

        # 남은 이동이 0일 때
        if remain == 0:
            if (cx, cy) == (r, c):
                result = ''.join(path)
                return True
            return False

        # d, l, r, u 순서로
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                need = abs(nx - r) + abs(ny - c)
                # 남은 이동으로 도달 가능해야 탐색
                if need <= remain - 1:
                    path.append(dirs[i])
                    if dfs(nx, ny, remain - 1):
                        return True
                    path.pop()

        return False

    dfs(x, y, k)
    return result if result else "impossible"
