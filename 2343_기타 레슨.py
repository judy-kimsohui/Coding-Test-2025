# 2343_기타 레슨

# N개의 강의, M개의 블루레이
N, M = map(int, input().split())
LectureL = list(map(int, input().split()))

# 블루레이의 최소 크기 = max(LectureL)
# 블루레이의 최대 크기 = sum(LectureL)
left, right = max(LectureL), sum(LectureL)
result = right

while left <= right:
    mid = (left + right) // 2  # 블루레이 크기 후보
    count = 1  # 필요한 블루레이 수
    temp = 0   # 현재 블루레이에 들어간 시간 합

    for time in LectureL:
        # 현재 강의가 mid 용량을 초과하면 새 블루레이로 넘어감
        if temp + time > mid:
            count += 1
            temp = time
        else:
            temp += time

    # 블루레이 개수가 많으면 → 용량이 너무 작다 → 키워야 함
    if count > M:
        left = mid + 1
    else:
        # M개 이하로 나눌 수 있다면 → 용량 줄여보기
        result = mid
        right = mid - 1

print(result)
