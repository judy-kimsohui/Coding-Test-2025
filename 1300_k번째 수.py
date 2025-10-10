# 1300_k번째 수

N = int(input())
K = int(input())

# A[i][j] = i×j
# B에서 오름차순 - k번째 수
# 배열 A와 B의 인덱스는 1부터 시작한다.

 
left, right = 1, K
result = 0

while left <= right:
    mid = (left + right) // 2
    
    # mid 이하의 원소 개수 세기
    count = 0
    for i in range(1, N + 1):
        count += min(mid // i, N)
    
    if count < K:
        left = mid + 1
    else:
        result = mid
        right = mid - 1

print(result)