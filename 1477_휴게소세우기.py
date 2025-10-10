# 1477_휴게소세우기

# N개의 휴게소 있음, M개 더 세울거임, 고속도로 길이 L
N, M, L = map(int, input().split())

# 현재 휴게소의 위치
ShopL = list(map(int, input().split()))
ShopL.append(0)
ShopL.append(L)
ShopL.sort()
NamuL = []
for i, shop in enumerate(ShopL):
    if i > 0:
        NamuL.append(ShopL[i] - ShopL[i-1])

NamuL.sort()

# 이미 휴게소가 있는 곳에 휴게소를 또 세울 수 없고, 고속도로의 끝에도 휴게소를 세울 수 없다.
# 휴게소가 없는 구간의 길이의 최댓값을 최소로 하려고 한다.

# 나무 자르는 간격 : mid
left = 1
right = NamuL[-1]
result = right

while left <= right:
    mid = (left + right) // 2

    # 세워야 하는 휴게소 수
    count = 0
    for x in NamuL:
        cut = (x - 1)//mid
        count += cut
    
    # 가장 큰 나무조각
    maxNamu = max([x%mid for x in NamuL] + [mid])
    
    # 세울 수 있는 휴게소가 더 많다면 -> 거리 늘려보기
    if count > M:
        left = mid + 1
    else:
        # M개 이하로 나눌 수 있다면 → 거리 줄여보기
        result = mid
        right = mid - 1

print(result)
