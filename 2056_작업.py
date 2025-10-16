# 2056_작업

from collections import defaultdict, deque

# 수행해야하는 작업 N개
# 각 작업마다 걸리는 시간

N = int(input())
TimeL = [0] * (N+1)

# 선후관계 표현 그래프
Graph = defaultdict(list)

indegree = [0] * (N+1)

# 결과값
Result = [0] * (N+1)

# i : 현재 작업 번호
for i in range(1, N+1):
    Input = list(map(int, input().split()))
    TimeL[i] = Input[0]

    # 선행 관계에 있는 작업들
    # Input[1] : 선행 작업 개수    
    for k in range(Input[1]):
        # Input[2+k] : 선행 작업 번호        
        Graph[Input[2+k]].append(i)
        # 진입차수 추가
        indegree[i] += 1

# print(Graph)

# 모든 작업을 완료하기 위한 최소 시간
# 진입차수가 0인 노드를 출발지로 하여, 시간을 점차 max를 기준으로 추가하고, 
# Result의 최대값을 출력한다.

Q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        Q.append(i)  
        Result[i] += TimeL[i]

while Q:
    node = Q.popleft()
    # print(Result)    
    for n in Graph[node]:
        Result[n] = max(Result[n], Result[node] + TimeL[n])
        indegree[n] -= 1        
        # 진입 차수가 0인 지점 = 새로운 탐색 구간
        if indegree[n] == 0:
            Q.append(n)
            


print(max(Result))



    
