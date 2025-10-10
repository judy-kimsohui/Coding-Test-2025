# 프로그래머스_2023_개인정보 수집 유효기간

# 개인정보는 유효기간이 지나면 파기해야한다.
# 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return

# 오늘 날짜를 의미하는 문자열 today,
# 약관의 유효기간을 담은 1차원 문자열 배열 terms
# 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies

def solution(today, terms, privacies):
    
    answer = []
    
    # 모든 달은 28일까지 있다
    TY, TM, TD = today.split(".")
    TY, TM, TD = int(TY), int(TM), int(TD)
    
    AlpL = [0] * 26
    for info in terms:
        Alp, tm = map(str, info.split())
        tm = int(tm)
        AlpL[ord(Alp)-65] = tm
    
    for i, info in enumerate(privacies):
        date, Alp = map(str, info.split())
        Y, M, D = date.split(".")
        Y, M, D = int(Y), int(M), int(D)
        
        # 지난 날
        if (TY-Y)*12*28 + (TM-M)*28 + TD-D >= AlpL[ord(Alp)-65]*28:
            answer.append(i+1)
            
    return answer