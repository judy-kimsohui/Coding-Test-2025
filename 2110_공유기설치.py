# 2110_공유기설치

# 수직선 상에 집들이 있다
# 집에 공유기를 설치해서, 인접한 공유기 사이 거리를 최대로 하자!

from bisect import bisect_left

# 집의 개수, 공유기의 개수
N, C = map(int, input().split())
HomeL = [int(input()) for _ in range(N)]
HomeL.sort()

# 최소 거리를 분배해서, 공유기 개수가 같으면 max를 조정해보자
left = 1
right = HomeL[-1] - HomeL[0]
result = 0

while left <= right:
    mid = (left+right) // 2
    
    # 세울 수 있는 공유기 개수 세기
    index = 0 # 첫 집에 공유기 세움
    count = 1
    while count < C:
        index = bisect_left(HomeL, HomeL[index] + mid)
        if index > N-1:
            break
        count += 1

    # 거리가 최대한 넓은걸 찾고 싶어!
    if count >= C:
        left = mid + 1
        # 더 넓혀
        result = max(result, mid)
    else:
        right = mid - 1

print(result)
    