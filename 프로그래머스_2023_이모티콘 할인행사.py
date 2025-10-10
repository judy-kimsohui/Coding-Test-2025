# 프로그래머스_2023_이모티콘 할인행사

from itertools import product

def solution(users, emoticons):
    
    # 이모티콘 플러스 서비스 가입 수와 이모티콘 매출액
    answer = []
    
    N = len(users)
    M = len(emoticons)
    # 이모티콘 개수 최대 7개
    
    # 할인율 : 10%, 20%, 30%, 40%
    discountL = [10, 20, 30, 40]
    EmoriconCaseL = list(product(discountL, repeat=M))
        
    RateL = []
    
    # 다음 기준에 따라 이모티콘을 사거나, 이모티콘 플러스 서비스에 가입
    for caseL in EmoriconCaseL:        
        EmoticonPlus = 0
        Money = 0
        
        for user_d, limit in users:
            Tobuy = 0
            
            # 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매    
            for i, price in enumerate(emoticons):
                discount = caseL[i]
                if discount >= user_d:
                    Tobuy += int(price*(100-discount)/100)
            if Tobuy < limit:
                Money += Tobuy
            
            # 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면,
            # 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입            
            else:
                EmoticonPlus += 1
                # Money += 5400
                
        # 각 케이스에 대한 이모티콘 플러스 가입수, 매출액 기록
        RateL.append([EmoticonPlus, Money])
    
    
    # 목표
    # 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
    # 이모티콘 판매액을 최대한 늘리는 것.    
    RateL = sorted(RateL, key=lambda x:(x[0], x[1]), reverse=True)
    answer = RateL[0]
    
    return answer