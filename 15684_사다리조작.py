# 15684 사다리조작
# 브루트포스 + 백트래킹 + 시뮬레이션 조합

from itertools import combinations

# N개의 세로선과, M개의 가로선
# 세로선마다 가로선을 놓을 수 있는 위치의 개수 H

# 사다리에 가로선을 추가해서, 사다리 게임의 결과를 조작하려고 한다. 
# i번 세로선의 결과가 i번이 나와야 한다. 추가해야 하는 가로선 개수의 최솟값

# 정답이 3보다 큰 값이면 -1을 출력한다. 또, 불가능한 경우에도 -1을 출력한다.
# index는 1부터 시작함

# 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H
N, M, H = map(int, input().split())

# Ladder[a][b] : b번째 세로선에 가로선이 a번째에 하나 있음
Ladder = [[0] * (H) for _ in range(N)]

# a, b (가로선 위치, 세로선 번호) - 입력되는 가로선이 서로 연속하는 경우는 없다.
for _ in range(M):
    garo, sero = map(int, input().split())
    sero -= 1
    garo -= 1
    Ladder[sero][garo] = +1     # 나가는 선
    Ladder[sero+1][garo] = -1   # 들어오는 선

# print(Ladder)

def check(n):
    t = n    # 세로선 위치 t
    for h in range(H):
        if Ladder[t][h] == +1:
            t += 1
        elif Ladder[t][h] == -1:
            t -= 1
    return t

CanDo = True
# Count = 0

# 1 ~ N번 세로선에 대해 i=i가 가능한지 확인
for n in range(N): 

    # 마지막이 t가 n일 경우, "성공"
    if check(n) == n:
        continue
    
    # 실패 - 선을 추가해야함
    else:
        CanDo = False
        # Count += 1  # 틀린 세로선 개수

# 0개 추가하고 한번에 성공
if CanDo:
    print(0)

else:
    # 사다리 가로 놓을 수 있는 위치 (1)
    Ladder1 = []
    for s in range(N-1):
        for h in range(H):
            if Ladder[s][h] == 0 and Ladder[s+1][h] == 0:
                Ladder1.append((s, h))

    answer = 4

    def is_ok():
        for i in range(N):
            if check(i) != i:
                return False
        return True

    def dfs(idx, cnt):
        global answer
        if cnt >= answer:
            return
        if is_ok():
            answer = cnt
            return
        if cnt == 3:
            return

        for i in range(idx, len(Ladder1)):
            s, h = Ladder1[i]
            if Ladder[s][h] != 0 or Ladder[s+1][h] != 0:
                continue

            Ladder[s][h] = +1
            Ladder[s+1][h] = -1
            dfs(i + 1, cnt + 1)
            Ladder[s][h] = 0
            Ladder[s+1][h] = 0

    dfs(0, 0)

    print(answer if answer <= 3 else -1)

