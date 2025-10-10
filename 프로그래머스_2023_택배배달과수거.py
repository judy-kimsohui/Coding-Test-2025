# 프로그래머스_2023_택배배달과수거

# 배달할 물건은 모두 크기가 같은 재활용 택배 상자에 담아 배달하며,
# 배달을 다니면서 빈 재활용 택배 상자들을 수거하려 합니다.

# 트럭에는 재활용 택배 상자를 최대 =cap=개 실을 수 있습니다. 
# 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리

def solution(cap, n, deliveries, pickups):
    
    answer = 0
    
    # deliveries 각 집마다 배달
    # pickups 각 집마다 수거    
    deliver = 0
    pickup = 0
    
    for i in range(n - 1, -1, -1):
        deliver += deliveries[i]
        pickup += pickups[i]
    
    # 아직 배달/수거할 게 남아있다면
        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            answer += (i + 1) * 2  # 왕복 거리
            
    return answer