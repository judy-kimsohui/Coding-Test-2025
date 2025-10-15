# 3665_최종순위

# n개의 팀, 1번부터 n번까지 번호 
# 팀 수는 500까지 
# 작년에 비해서 상대적인 순위가 바뀐 팀의 목록만 발표 
# 올해 최종 순위는? 

# 확실한 올해 순위를 만들 수 없는 경우가 있을 수도 있고, 
# 일관성이 없는 잘못된 정보일 수도 있다. # 엥? ㅋㅋ

from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    Rank = list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    # 1. 작년 순위로 그래프 생성
    # 순위 별 노드 확인 ~
    for i in range(n):
        for j in range(i + 1, n):
            # Rank[i] : i번째 순위에 해당하는 노드 번호
            # Rank[j] : i번째 순위 이상의 노드 번호
            
            # 지금 번호(i번째 순위)보다 순위가 낮은 노드들 추가
            graph[Rank[i]].append(Rank[j])

            # 낮은 번호로 판명난 아이들은 진입 차수 추가
            indegree[Rank[j]] += 1

    # 2. 순위 변경 반영
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        # 만약 b가 a보다 순위가 낮았다면 b의 순위를 a보다 높인다
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            
            # 진입 차수를 변경한다
            indegree[a] += 1
            indegree[b] -= 1
        
        # 만약 b가 a보다 순위가 높았다면 b의 순위를 a보다 낮춘다
        else:
            graph[b].remove(a)
            graph[a].append(b)

            # 진입 차수를 변경한다
            indegree[b] += 1
            indegree[a] -= 1

    # 3. 위상정렬 수행
    q = deque()
    
    # 진입 차수가 0인 부분을 Q에 저장
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 결과 저장용 리스트
    result = []
    
    # 확인 다했음? 판별 플래그
    certain = True

    # 가능함? 판별 플래그
    impossible = False

    # 노드 번호만큼 실행
    for _ in range(n):
        
        # 큐에 남은 노드가 없음 (노드 개수만큼 확인 불가능 = 순위 설정 불가능)
        if not q:
            impossible = True
            break

        # 큐에 노드가 여러개 있음 (순위가 확실하지 않음)
        if len(q) > 1:
            certain = False

        # Q의 노드 하나 = 꺼내서 결과에 저장
        now = q.popleft()
        result.append(now)
        
        # 다음 부분 확인 후 진입차구 감소
        for nxt in graph[now]:
            indegree[nxt] -= 1
            
            # 진입 차수가 0이 된다면 Q에 넣기
            if indegree[nxt] == 0:
                q.append(nxt)

    # 불가능했음
    if impossible:
        print("IMPOSSIBLE")
    
    # certain이 false - 확인을 덜함
    elif not certain:
        print("?")
    
    # 모든 노드 확인함 - 순위 결정남
    else:
        print(*result)
