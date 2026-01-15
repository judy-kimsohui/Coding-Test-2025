from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    MAX = 102
    filled = [[0] * MAX for _ in range(MAX)]
    map2L  = [[0] * MAX for _ in range(MAX)]  # 테두리만 2로 담을 맵

    
    characterX *= 2; characterY *= 2; itemX *= 2; itemY *= 2
    
    # 사각형 안 모두 같은 숫자 1로 채움
    for sr, sc, er, ec in rectangle:
        sr *= 2; sc *= 2; er *= 2; ec *= 2
        for r in range(sr, er+1):
            for c in range(sc, ec+1):
                filled[r][c] = 1
    
    # 바깥 경로 지정
    for i in range(1, MAX):
        for k in range(1, MAX):
            
            if filled[i][k] != 1:
                continue
                
             # 상하좌우가 모두 1이면 내부
            if filled[i-1][k] == 1 and filled[i+1][k] == 1 and filled[i][k-1] == 1 and filled[i][k+1] == 1:
                map2L[i][k] = 1
                continue
            else:
                map2L[i][k] = 2 # 테두리
            
    # 안쪽 꼭지점
    for i in range(1, MAX):
        for k in range(1, MAX):
            if map2L[i][k] == 1:
                if map2L[i-1][k-1] == 0 and map2L[i][k-1] == 2 and map2L[i-1][k] == 2 and map2L[i][k] == 1: 
                    map2L[i][k] = 2 
                elif map2L[i-1][k+1] == 0 and map2L[i-1][k] == 2 and map2L[i][k+1] == 2 and map2L[i][k] == 1: 
                    map2L[i][k] = 2 
                elif map2L[i+1][k-1] == 0 and map2L[i][k-1] == 2 and map2L[i+1][k] == 2 and map2L[i][k] == 1: 
                    map2L[i][k] = 2 
                elif map2L[i+1][k+1] == 0 and map2L[i+1][k] == 2 and map2L[i][k+1] == 2 and map2L[i][k] == 1: 
                    map2L[i][k] = 2

    # for i, lineL in enumerate(map2L):
    #     print(lineL[0:50])
        
    # 시작점 ~ 종료지점
    # 중간에 꺾이는 부분을 확인해야함
    
    start = (characterX, characterY)
    end = (itemX, itemY)
    
    visited2L = [[-1] * MAX for _ in range(MAX)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    
    visited2L[characterX][characterY] = 1
    Q = deque([(start, 0)])
    
    AnsL = [50]
    
    while Q:
        (r, c), dist = Q.popleft()
        # print(r, c, dist)

        if (r, c) == (itemX, itemY):
            return dist//2
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 < nr < MAX and 0 < nc < MAX and visited2L[nr][nc] == -1:

                # 둘레길
                if map2L[nr][nc] == 2:
                    Q.append(((nr, nc), dist+1))
                    visited2L[nr][nc] = 1
                    
    return min(AnsL)
