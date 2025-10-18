# 17144_미세먼지안녕!

# 공기청정기는 항상 1번 열에 설치됨
# (r, c)에 있는 미세먼지의 양은 Ar,c

# 1초 동안 아래 적힌 일이 순서대로 일어난다.

# 미세먼지 확산
# 인접 4방향으로 확산 (공기청정기 방향 제외)
# 확산되는 양은 Ar,c//5
# (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수)

# 공기청정기 작동
# 공기청정기가 설치된 곳은 Ar,c가 -1
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환
# 미세먼지가 바람의 방향대로 모두 한 칸씩 이동

# T초가 지난 후 방에 남아있는 미세먼지의 양

from collections import deque

R, C, T = map(int, input().split())
Map2L = []
Result2L = []
GL = [] # 공기청정기 위치
ML = [] # 미세먼지 위치

# 입력
for r in range(R):
    Input = list(map(int, input().split()))
    Map2L.append(Input[:])    
    Result2L.append(Input[:])    
    for c in range(C):
        # 공기청정기 위치 등록
        if Input[c] == -1:
            GL.append((r, c))
        # 미세먼지 위치 등록
        if Input[c] > 0:
            ML.append((r, c))

# print(GL, ML)
# print(Map2L)


# for cl in Result2L:
#     print(*cl)
# print()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):

    # 미세먼지 퍼지기
    NS = set(ML)
    Q = deque(ML)
    while Q:
        (mr, mc) = Q.popleft()
        count = 0
        Amount = Map2L[mr][mc]
        for i in range(4):
            x, y = mr + dx[i], mc + dy[i]
            if 0 <= x < R and 0 <= y < C and (x, y) != (GL[0][0], GL[0][1]) and (x, y) != (GL[1][0], GL[1][1]):                
                Result2L[x][y] += Amount//5
                count += 1
                NS.add((x, y))
        Result2L[mr][mc] -= (Amount//5) * count
    
    ML = list(NS)
    
    # 공기청정기 작동
    CleanL = ["0c", "-1c", "0r", "-1r", "가운데 두줄"]


    # 위쪽 공기청정기
    # c0 아래쪽으로 한칸 이동
    for r in range(GL[0][0]-1, 0, -1):
        Result2L[r][0] = Result2L[r-1][0]
    # ← 위쪽 줄
    for c in range(C-1):
        Result2L[0][c] = Result2L[0][c+1]
    # → 오른쪽 세로
    for r in range(0, GL[0][0]):
        Result2L[r][-1] = Result2L[r+1][-1]
    # ↓ 아래쪽 줄
    for c in range(C-1, 1, -1):
        Result2L[GL[0][0]][c] = Result2L[GL[0][0]][c-1]
    Result2L[GL[0][0]][1] = 0
    Result2L[GL[0][0]][0] = -1


    # 아래쪽 공기청정기
    # c0 위쪽으로 한칸 이동
    for r in range(GL[1][0]+1, R-1):
        Result2L[r][0] = Result2L[r+1][0]
    # → 아랫줄
    for c in range(C-1):
        Result2L[R-1][c] = Result2L[R-1][c+1]
    # ↑ 오른쪽 세로
    for r in range(R-1, GL[1][0], -1):
        Result2L[r][-1] = Result2L[r-1][-1]
    # ← 윗줄
    for c in range(C-1, 1, -1):
        Result2L[GL[1][0]][c] = Result2L[GL[1][0]][c-1]
    Result2L[GL[1][0]][1] = 0
    Result2L[GL[1][0]][0] = -1


    # 새로운 정보 반영
    for r in range(R):
        for c in range(C):
            Map2L[r][c] = Result2L[r][c]

    # for cl in Result2L:
    #     print(*cl)
    # print()

Answer = 0
for column in Result2L:
    Answer += sum(column)

print(Answer+2)
