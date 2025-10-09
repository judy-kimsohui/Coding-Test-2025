# 프로그래머스_무지의먹방

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    foods = sorted([(time, idx+1) for idx, time in enumerate(food_times)])
    
    prev = 0
    n = len(food_times)
    for i, (time, _) in enumerate(foods):
        spend = (time - prev) * (n - i)
        if k >= spend:
            k -= spend
            prev = time
        else:
            remain = sorted(foods[i:], key=lambda x: x[1])
            return remain[k % (n - i)][1]
    return -1
