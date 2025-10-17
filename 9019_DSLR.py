# 9019_DSLR
# 스페셜 저지!!

# 레지스터 n에 0~9999 값 저장
# 네자릿수 d1, d2, d3, d4

# A와 B(A ≠ B)에 대하여 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램
# 가능한 명령어 나열이 여러 개면, 아무거나 출력 (예: LL 이나 RR)

from collections import deque

# DSLR 네 가지 연산 정의
def D(n):
    # D: n을 두배로. 10000 이상인 경우 나눈 나머지
    return (2 * n) % 10000

def S(n):
    # S: n-1, 단 0이라면 9999
    return 9999 if n == 0 else n - 1

def L(n):
    # L: 왼쪽으로 1회전
    # 예) 1234 → 2341
    return (n % 1000) * 10 + n // 1000

def R(n):
    # R: 오른쪽으로 1회전
    # 예) 1234 → 4123
    return (n // 10) + (n % 10) * 1000


# 테스트 케이스 개수
N = int(input())

for _ in range(N):
    # A > B
    A, B = map(int, input().split())

    # BFS를 위한 큐 초기화
    Q = deque([(A, "")])

    # 방문 배열: 0~9999
    visited = [False] * 10000
    visited[A] = True

    # BFS 탐색 시작
    while Q:
        # 현재 값과 지금까지의 명령어 시퀀스
        n, result = Q.popleft()

        # 목표 값 도달 시 출력
        if n == B:
            print(result)
            break

        # D 연산
        nd = D(n)
        if not visited[nd]:
            visited[nd] = True
            Q.append((nd, result + "D"))

        # S 연산
        ns = S(n)
        if not visited[ns]:
            visited[ns] = True
            Q.append((ns, result + "S"))

        # L 연산
        nl = L(n)
        if not visited[nl]:
            visited[nl] = True
            Q.append((nl, result + "L"))

        # R 연산
        nr = R(n)
        if not visited[nr]:
            visited[nr] = True
            Q.append((nr, result + "R"))
