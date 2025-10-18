# (틀림)

# 17779_게리맨더링2

# N×N인 격자, r행 c열, (r, c)
# 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다.

# 다섯 개의 선거구로 나누기
# 선거구를 나누는 방법 중에서, 
# 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 구해보자.
# 구역 (r, c)의 인구는 A[r][c]

# 5 ≤ N ≤ 20

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 10**9

for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 >= N:
                    continue
                if y - d1 < 0 or y + d2 >= N:
                    continue

                zone = [[0]*N for _ in range(N)]

                # 경계선 표시
                for i in range(d1 + 1):
                    zone[x + i][y - i] = 5
                    zone[x + d2 + i][y + d2 - i] = 5
                for i in range(d2 + 1):
                    zone[x + i][y + i] = 5
                    zone[x + d1 + i][y - d1 + i] = 5

                # 내부 채우기
                for r in range(x + 1, x + d1 + d2):
                    fill = False
                    for c in range(N):
                        if zone[r][c] == 5:
                            fill = not fill
                        if fill:
                            zone[r][c] = 5

                pop = [0]*5
                for r in range(N):
                    for c in range(N):
                        if zone[r][c] == 5:
                            pop[4] += A[r][c]
                        elif 0 <= r < x + d1 and 0 <= c <= y:
                            pop[0] += A[r][c]
                        elif 0 <= r <= x + d2 and y < c < N:
                            pop[1] += A[r][c]
                        elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                            pop[2] += A[r][c]
                        elif x + d2 < r < N and y - d1 + d2 <= c < N:
                            pop[3] += A[r][c]

                ans = min(ans, max(pop) - min(pop))

print(ans)
