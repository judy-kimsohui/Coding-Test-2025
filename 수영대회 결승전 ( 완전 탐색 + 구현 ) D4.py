# 수영대회 결승전 ( 완전 탐색 + 구현 ) D4

# 가로 N 세로 N만큼 공간
# 섬과 같은 지나갈 수 없는 장애물(1)과, 주기적으로 사라졌다 나타나는 소용돌이(2)

# 소용돌이는 생성되고 2초동안 유지되다가 1초동안 잠잠해진다.
    # 예를들어, 0초에 생성된 소용돌이는 0초, 1초까지 유지되고 2초에 사라지게된다.
    # 또한 3초, 4초에는 생성되고 5초에 사라진다.
    # 한번 통과한 소용돌이 위에서는 머물러 있을 수 있다.

# 바다에서 삼성이를 우승시키려면 어떤 경로로 보내야 될까?

from collections import deque

T = int(input())
for t in range(T):
    print("#" + str(t+1), end=" ")
    
    # N : 칸 수, M : 스프레이 분사 세기
    N = int(input())
    List = [list(map(int, input().split())) for _ in range(N)]
    sr, sc = map(int, input().split()) # 시작점
    er, ec = map(int, input().split()) # 도착점   

    # sr, sc = sr-1, sc-1
    # er, ec = er-1, ec-1
    
    Time = 0
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    
    # 큐
    Q = deque([(sr, sc, Time)])

    # 방문기록
    visitedL = [[0] * N for _ in range(N)]
    visitedL[sr][sc] = 1
    
    while Q:
        (r, c, t) = Q.popleft()
        if (r, c) == (er, ec):
            Time = t
            break

        # 현재 시간 t초
        # 째깍 - 1초가 흐를 예정이다
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # 경계선 안에 있고, 장애물이 아니며, 방문하지 않은 경우 -
            if 0 <= nr < N and 0 <= nc < N and List[nr][nc] != 1 and visitedL[nr][nc] == 0:
                # 다음 칸이 일반 칸인 경우
                if List[nr][nc] == 0:
                    visitedL[nr][nc] = 1
                    Q.append((nr, nc, t+1))

                # 다음 칸이 소용돌이 칸인 경우
                elif List[nr][nc] == 2:
                    # 다음 턴에 소용돌이가 사라진다면, 지나갈 수 있음
                    if (t+1) % 3 == 0:
                        visitedL[nr][nc] = 1
                        Q.append((nr, nc, t+1))
                    else:
                        Q.append((r, c, t+1))
                        
    if Time == 0:
        print("-1")
    else:
        print(Time)
              



    