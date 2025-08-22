"""
메모리 초과 안 나는 코드 (DFS + 비트마스크)
"""

# 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
    # 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있다.
    # 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
# 말이 최대한 몇 칸을 지날 수 있는지를 구하자

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)] 

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

max_len = 1

def dfs(x, y, visited, cnt):
    global max_len
    max_len = max(max_len, cnt)
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < C and 0 <= ny < R:
            idx = ord(board[ny][nx]) - 65
            
            # 사용한 알파벳인지 확인 : 1 << idx → idx번째 비트만 1인 값
            if not (visited & (1 << idx)):                
                # 새로운 알파벳을 사용했다고 표시 : OR 연산 → visited에 idx번째 비트를 켜서(1로 만들어서) 새 알파벳을 사용했다고 표시
                dfs(nx, ny, visited | (1 << idx), cnt + 1)

start_idx = ord(board[0][0]) - 65
# 시작 칸의 알파벳을 방문했다고 표시
dfs(0, 0, 1 << start_idx, 1)
print(max_len)
