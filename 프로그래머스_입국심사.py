# 프로그래머스_입국심사


# 모든 사람이 심사를 받는데 걸리는 최소 시간
# 입국을 기다리는 사람 수 n
# 각 심사관이 한 명을 심사하는데 "걸리는 시간" 배열
# line : Time
# count : people

def solution(n, times):
    
    result = 0
    
    # 입국 심사관 몇 명?
    L = len(times)

    # Time
    small = 0
    big = n * max(times)
    
    while small <= big:
        Time = (small + big)//2
        People = 0
        
        # 시간에 대해 심사 가능한 사람 수 찾아보자
        for Judge in times:
            People += Time // Judge
        
        # 사람에 대해 시간이 최소가 되게
        if People >= n:
            big = Time-1
            result = Time
        else:
            small = Time+1    
            
    return result
