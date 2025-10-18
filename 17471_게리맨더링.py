# 17471_게리맨더링

# 인구가 1번 구역부터 N번 구역까지 있음
# 두 개의 선거 구역으로 나눔

from itertools import combinations
from collections import defaultdict, deque

N = int(input())
PeopleL = [0] + list(map(int, input().split()))

Graph = defaultdict(list)
for i in range(1, N+1):
    
    # 인접 정보
    Input = list(map(int, input().split()))

    # 양방향 입력
    for num in Input[1:]:
        if num not in Graph[i]:
            Graph[i].append(num)
        if i not in Graph[num]:
            Graph[num].append(i)

ChunkL = [i for i in range(1, N+1)]
ChunkS = set(ChunkL)

# 인구 차이 최소값
MinSub = float("inf")
for n in range(1, N//2 + 1):
    
    # 2개로 나눌 모든 경우의 수를 찾자
    CaseL = combinations(ChunkL, n)
    for case in CaseL:

        caseAS = set(case)
        caseBS = ChunkS - caseAS
        

        # A 구역이 인접해있는지 확인
        start, ChunkA = case[0], True    
        CheckAS = {start}
        VisitedAL = [0] * (N+1)
        VisitedAL[start] = 1       
        Q = deque([start])
        while Q:
            node = Q.popleft()            
            for next in Graph[node]:
                if next in caseAS and VisitedAL[next] == 0:
                    CheckAS.add(next)
                    Q.append(next)
                    VisitedAL[next] = 1
        if CheckAS != caseAS:
            ChunkA = False
        
        # B 구역이 인접해있는지 확인
        start, ChunkB = list(caseBS)[0], True
        CheckBS = {start}
        VisitedBL = [0] * (N+1)
        VisitedBL[start] = 1      
        Q = deque([start])
        while Q:
            node = Q.popleft()            
            for next in Graph[node]:
                if next in caseBS and VisitedBL[next] == 0:
                    CheckBS.add(next)
                    Q.append(next)
                    VisitedBL[next] = 1        
        if CheckBS != caseBS:
            ChunkB = False

        # 인구차이 확인
        if ChunkA and ChunkB:
            # print(caseAS, CheckAS, caseBS)
            SumA, SumB = 0, 0
            for a in caseAS:
                SumA += PeopleL[a]
            for b in caseBS:
                SumB += PeopleL[b]
            
            
            Sub = abs(SumA-SumB)
            
            # print(SumA, SumB)
            MinSub = min(MinSub, Sub)

if MinSub != float("inf"):
    print(MinSub)

# 두 선거구로 나눌 수 없다
else:
    print("-1")

