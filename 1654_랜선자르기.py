# 1654_랜선자르기
# 가지고 있는 랜선 개수, 필요한 랜선 개수
import bisect

K, N = map(int, input().split())
LineL = [int(input()) for _ in range(K)]

# 만들 수 있는 최대 랜선의 길이 출력
left, right = 1, max(LineL)
result = 0

while left <= right:
    mid = (left + right) // 2
    count = sum(x // mid for x in LineL)
    if count < N:
        right = mid - 1        
    else:
        result = max(result, mid)
        left = mid + 1
        

print(result)