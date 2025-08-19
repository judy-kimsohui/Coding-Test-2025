# 크기가 N X M인 지도
# 주사위 지도 위 좌표 (r,c)
# 놓여져 있는 곳의 좌표는 (x, y) 이다.

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다.

# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
    # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다
    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    # 주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

# 주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 
    # 주사위가 이동했을 때 마다 주사위 윗면에 쓰여 있는 값을 구하는 프로그램을 작성하시오.
    # 이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다.
  
  
# N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다.

N, M, x, y, K = map(int, input().split())
MapL = []
for _ in range(N):
    MapL.append(list(map(int, input().split())))

JusawiL = [[-1, 0, -1], [0, 0, 0], [-1, 0, -1], [-1, 0, -1]]
DSBN = [1, 2, 3, 4]

def RoundD_F(Jusawi):
    Jusawi[1][0], Jusawi[1][1], Jusawi[1][2], Jusawi[3][1] = Jusawi[1][1], Jusawi[1][2], Jusawi[3][1], Jusawi[1][0]
    return Jusawi

def RoundS_F(Jusawi):
    Jusawi[1][0], Jusawi[1][1], Jusawi[1][2], Jusawi[3][1] = Jusawi[3][1], Jusawi[1][0], Jusawi[1][1], Jusawi[1][2]
    return Jusawi

def RoundB_F(Jusawi):
    Jusawi[0][1], Jusawi[1][1], Jusawi[2][1], Jusawi[3][1] = Jusawi[3][1], Jusawi[0][1], Jusawi[1][1], Jusawi[2][1]
    return Jusawi

def RoundN_F(Jusawi):
    Jusawi[0][1], Jusawi[1][1], Jusawi[2][1], Jusawi[3][1] = Jusawi[1][1], Jusawi[2][1], Jusawi[3][1], Jusawi[0][1]
    return Jusawi

# 초기 주사위 설정
if MapL[x][y] == 0:
    MapL[x][y] = JusawiL[1][1]
else:
    JusawiL[1][1] = MapL[x][y]
    MapL[x][y] = 0

# 명령어 입력
MungL = list(map(int, input().split()))
for k in MungL:        
    # 동서남북 주사위 이동
    # 만약 이동을 할 수 없을 경우 명령어 생략
    moved = False
    
    if k == 1: # 동 +y
        if y + 1 < M:
            moved = True
            y += 1
            JusawiL = RoundD_F(JusawiL)
    elif k == 2: # 서 -y
        if y - 1 >= 0:
            moved = True
            y -= 1
            JusawiL = RoundS_F(JusawiL)
    elif k == 3: # 북 -x
        if x - 1 >= 0:
            moved = True
            x -= 1
            JusawiL = RoundB_F(JusawiL)
    elif k == 4: # 남 +x
        if x + 1 < N:
            moved = True
            x += 1
            JusawiL = RoundN_F(JusawiL)
    
    # 주사위 윗면 : Jusawi[3][1]
    # 주사위 바닥면 : Jusawi[1][1]
        # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다
        # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    
    # 주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
    if moved:
        if MapL[x][y] == 0:
            MapL[x][y] = JusawiL[1][1]
        else:
            JusawiL[1][1] = MapL[x][y]
            MapL[x][y] = 0
    
        print(JusawiL[3][1])