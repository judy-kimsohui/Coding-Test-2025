"""
메모리 초과!!
"""



# 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
    # 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있다.
    # 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
# 말이 최대한 몇 칸을 지날 수 있는지를 구하자

from collections import deque

# 보드 정의
R, C = map(int, input().split())
BoardL = []
for _ in range(R):
    BoardL.append(list(input()))

# 초기값 설정
start = (0, 0)
end = (C-1, R-1)
startN = BoardL[0][0]

# A:65, Z:90 26개
S_CheckApL = [0] * 26
S_CheckApL[ord(startN)-65] = 1
S_VisitedL = [[False] * C for _ in range(R)]
S_VisitedL[0][0] = True

# 결과값
Result = 1

# 큐 정의
Q = deque([(start, startN, S_CheckApL, S_VisitedL)])
while Q:
    (x, y), num, CheckApL, VisitedL = Q.popleft()
    if (x, y) == end:
        break
        
    # 네 방향으로 탐색
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]        
                
        # 보드 유효값 검증
        if 0 <= ny < R and 0 <= nx < C and VisitedL[ny][nx] == False:

            # 알파벳 : BoardL[ny][nx]
            NewNum = BoardL[ny][nx]

            # 알파벳 인덱스 : ord(BoardL[ny][nx])-65
            IDX = ord(NewNum)-65

            # 조건 : 만약 같은 알파벳이라면, 길을 끝내고 최대 길이와 비교한다
            if CheckApL[IDX] == 1:
                Result = max(Result, CheckApL.count(1))
            
            # 조건2: 새로운 알파벳이라면, 새로운 길을 추가한다! (복사하고 수정해서 추가하기)
            else:
                NewCheckApL = CheckApL[:]
                NewCheckApL[IDX] = 1
                
                NewVisitedL = [row[:] for row in VisitedL]
                NewVisitedL[ny][nx] = True
                
                # 큐에 추가
                Q.append(((nx, ny), NewNum, NewCheckApL, NewVisitedL))
        
print(Result)