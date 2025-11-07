# 시간초과

# N, M = map(int, input().split())

# Table = []
# for _ in range(N):
#     Table.append(list(map(int, input().split())))

# Result = []

# for t in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
#     Sum = 0
#     for x in range(x1, x2+1):
#         Sum += sum(Table[x][y1:y2+1])
    
#     Result.append(Sum)

# for r in Result:
#     print(r)
    
    
    
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 1-based indexing을 쓰기 위해 (N+1)x(N+1) 배열 생성
Table = [[0] * (N + 1)]
for _ in range(N):
    Table.append([0] + list(map(int, input().split())))

# 누적합 배열 생성
Prefix = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        Prefix[i][j] = (
            Table[i][j]
            + Prefix[i - 1][j]
            + Prefix[i][j - 1]
            - Prefix[i - 1][j - 1]
        )

# 쿼리 처리
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = (
        Prefix[x2][y2]
        - Prefix[x1 - 1][y2]
        - Prefix[x2][y1 - 1]
        + Prefix[x1 - 1][y1 - 1]
    )
    print(result)
