# 프로그래머스_징검다리

# 사이에 바위들이 놓여있다

def solution(distance, rocks, n):
    
    small = 0
    big = distance
    result = 0
    rocks.sort()
    rocks.append(distance)
    # print(rocks)
    
    while small <= big:
        mid = (small + big)//2
        
        # mid거리보다 사이 간격이 좁으면, 없애버린다        
        Rock = 0    # 제거한 돌 수         
        back = 0    # 이전 돌 위치
        Min = distance # 최소 간격
        
        for rock in rocks:            
            dist = rock - back    
            # print(rock, back, dist)
            
            # 돌 사이 간격이 좁네? 없애장
            if dist < mid:
                Rock += 1
            # 돌 사이 간격이 이미 넓다.. 넘어가자
            else:
                Min = min(Min, dist)
                back = rock

        # 제거한 바위 수가 기준보다 적거나 같으면, 바위를 더 제거해야지 거리를 더 늘려
        if Rock <= n:
            small = mid + 1
            result = max(Min, result)
        else:
            big = mid -1
                    
    return result