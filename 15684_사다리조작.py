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
    # 가로선을 추가하여, 성공 여부 확인
    # 3개를 초과하면 안됨
    # print(Count)
    
    # 사다리 가로 놓을 수 있는 위치 (1)
    Ladder1 = []
    for s in range(N-1):
        for h in range(H):
            if Ladder[s][h] == 0:
                Check = False
                if s == 0 and Ladder[s+1][h] == 0:
                    Check = True
                elif s == N-1 and Ladder[s-1][h] == 0:
                    Check = True
                else:
                    if Ladder[s-1][h] == 0 and Ladder[s+1][h] == 0:
                        Check = True                
                if Check:
                    Ladder1.append((s, h))
    # print(Ladder1)
    
    # 사다리 가로 놓을 수 있는 위치 (2)
    Ladder2 = []
    Ladder2Check = list(combinations(Ladder1, 2))
    for ((s1, h1), (s2, h2)) in Ladder2Check:
        if not (h1 == h2 and abs(s1-s2) == 1):        
            Ladder2.append(((s1, h1), (s2, h2)))
    
    # 사다리 가로 놓을 수 있는 위치 (1+2)
    Ladder3 = []
    for ((s1, h1), (s2, h2)) in Ladder2:
        for (s3, h3) in Ladder1:            
            # 같은 위치는 아예 제외
            if (s3, h3) == (s1, h1) or (s3, h3) == (s2, h2):
                continue
            
            # 서로 인접한 가로선이 생기면 안 됨
            if h1 == h3 and abs(s1 - s3) == 1:
                continue
            if h2 == h3 and abs(s2 - s3) == 1:
                continue
            
            Ladder3.append(((s1, h1), (s2, h2), (s3, h3)))
                    
    # 1~3개 Bruteforce
    for n in range(1, 4):
        if n == 1:
            for s1, h1 in Ladder1:
                Ladder[s1][h1] = +1     # 나가는 선
                Ladder[s1+1][h1] = -1   # 들어오는 선

                # 1 ~ N번 세로선에 대해 i=i가 가능한지 확인
                CanDo = True
                for n in range(N): 

                    # 마지막이 t가 n일 경우, "성공"
                    if check(n) == n:
                        continue
                    
                    # 실패 - 선을 추가해야함
                    else:
                        CanDo = False

                if CanDo:
                    print(1)
                    exit(0)
                else:
                    Ladder[s1][h1] = 0     # 나가는 선
                    Ladder[s1+1][h1] = 0   # 들어오는 선
            
        elif n == 2:
            for ((s1, h1), (s2, h2)) in Ladder2:
                Ladder[s1][h1] = +1     # 나가는 선
                Ladder[s1+1][h1] = -1   # 들어오는 선
                
                Ladder[s2][h2] = +1     # 나가는 선
                Ladder[s2+1][h2] = -1   # 들어오는 선

                # 1 ~ N번 세로선에 대해 i=i가 가능한지 확인
                CanDo = True
                for n in range(N): 

                    # 마지막이 t가 n일 경우, "성공"
                    if check(n) == n:
                        continue
                    
                    # 실패 - 선을 추가해야함
                    else:
                        CanDo = False

                if CanDo:
                    print(2)
                    exit(0)
                else:
                    Ladder[s1][h1] = 0     # 나가는 선
                    Ladder[s1+1][h1] = 0   # 들어오는 선
                    
                    Ladder[s2][h2] = 0     # 나가는 선
                    Ladder[s2+1][h2] = 0   # 들어오는 선            
            
        elif n == 3:
            for ((s1, h1), (s2, h2), (s3, h3)) in Ladder3:
                Ladder[s1][h1] = +1     # 나가는 선
                Ladder[s1+1][h1] = -1   # 들어오는 선
                
                Ladder[s2][h2] = +1     # 나가는 선
                Ladder[s2+1][h2] = -1   # 들어오는 선

                Ladder[s3][h3] = +1     # 나가는 선
                Ladder[s3+1][h3] = -1   # 들어오는 선

                # 1 ~ N번 세로선에 대해 i=i가 가능한지 확인
                CanDo = True
                for n in range(N): 

                    # 마지막이 t가 n일 경우, "성공"
                    if check(n) == n:
                        continue
                    
                    # 실패 - 선을 추가해야함
                    else:
                        CanDo = False

                if CanDo:
                    print(3)
                    exit(0)
                else:
                    Ladder[s1][h1] = 0     # 나가는 선
                    Ladder[s1+1][h1] = 0   # 들어오는 선
                    
                    Ladder[s2][h2] = 0     # 나가는 선
                    Ladder[s2+1][h2] = 0   # 들어오는 선
            
                    Ladder[s3][h3] = 0     # 나가는 선
                    Ladder[s3+1][h3] = 0   # 들어오는 선
            
    print(-1)


