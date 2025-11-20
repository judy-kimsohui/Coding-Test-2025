# 14503 로봇청소기 Gold 5

# 로봇 청소기와 방의 상태, 청소하는 영역의 개수
# N X M (r, c)

# 입력
# 1 : 벽
N, M = map(int, input().split())
r, c, d = map(int, input().split())
RoomL = []
for _ in range(N):
    RoomL.append(list(map(int, input().split())))

# 0 북, 1 동, 2 남, 3 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 로봇 청소기 위치
nowR, nowC = r, c

# 방향 (인덱스)
nowD = d

Count = 0
# print("nowD : " + str(nowD))
# print("nowR : " + str(nowR))
# print("nowC : " + str(nowC))   

while True:
    
    # 현재 칸이 아직 청소되지 않은 경우, 청소
    if RoomL[nowR][nowC] == 0:
        RoomL[nowR][nowC] = 2
        Count += 1

        # print("----------------------------------")
        # print("----------------------------------")
        # for i in range(N):
        #     print(*RoomL[i])
    
    else:        
        # 방이 모두 청소되었는지 확인 플래그
        CheckClean = True
        for i in range(4):
            nr, nc = nowR + dr[i], nowC + dc[i]
            
            # 청소해야하는 칸이 있는 경우 플래그는 Fasle
            if 0 <= nr < N and 0 <= nc < M and RoomL[nr][nc] == 0:
                CheckClean = False
        
        # 주변 4칸이 모두 청소된 경우 후진 
        if CheckClean == True:
            nowR += dr[(nowD+2)%4]
            nowC += dc[(nowD+2)%4]
            
            # - 후진이 불가능하면 작동을 멈추고, 청소한 칸의 개수 출력
            if 0 <= nowR < N and 0 <= nowC < M:
                if RoomL[nowR][nowC] == 1:
                    break
        
        # 주변 4칸 중 청소가 필요한 칸이 있는 경우
        else:            
            # - 반시계 방향으로 (북 -> 서 -> 남 -> 동) 90도 회전
            nowD = (nowD + 3)%4
            # print("*")         
            
            nr = nowR + dr[nowD]
            nc = nowC + dc[nowD]            
            
            if 0 <= nr < N and 0 <= nc < M:
            # - 회전한곳 앞이 청소되지 않은 칸인 경우 앞쪽 칸으로 전진
                if RoomL[nr][nc] == 0:
                    nowR, nowC = nr, nc
                    # print("nowD : " + str(nowD))
                    # print("nowR : " + str(nowR))
                    # print("nowC : " + str(nowC))   

# print("----------------------------------")
print(Count)

    
    