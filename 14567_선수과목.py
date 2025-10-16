# 14567_선수과목

# 수강 과목 N개
# 선수조건 수 M

from collections import defaultdict, deque

N, M = map(int, input().split())

# 선후관계 표현 그래프
Graph = defaultdict(list)

indegree = [0] * (N+1)

# 결과값
Result = [0] * (N+1)

# i : 현재 과목 번호
for i in range(1, M+1):
    a, b = map(int, input().split())
    
    # a가 b의 선수과목
    Graph[a].append(b)
            
    # 진입차수 추가
    indegree[b] += 1

# print(Graph)

# 1번 과목부터 N번 과목까지 차례대로 최소 몇 학기에 이수할 수 있는지
Q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        Q.append(i)  
        Result[i] += 1

while Q:
    node = Q.popleft()
    # print(Result)    
    for n in Graph[node]:
        Result[n] = max(Result[n], Result[node] + 1)
        indegree[n] -= 1        
        # 진입 차수가 0인 지점 = 새로운 탐색 구간
        if indegree[n] == 0:
            Q.append(n)
        
print(*Result[1:])



    
