# 2805_나무자르기

from bisect import bisect_left

# 나무의 수, 집으로 가져가려하는 나무 길이 M
N, M = map(int, input().split())
NamuL = list(map(int, input().split()))
NamuL.sort()

# 절단할 수 있는 높이의 최대값
start = 0
end = max(NamuL)
result = 0

while start <= end:
    mid = (start+end) // 2
    index = bisect_left(NamuL, mid)
    check = sum(NamuL[index:]) - (N-index) * mid    
    if M <= check:
        start = mid + 1
        result = max(result, mid)
    else:        
        end = mid - 1

print(result)