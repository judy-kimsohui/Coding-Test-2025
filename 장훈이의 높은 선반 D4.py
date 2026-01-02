# 장훈이의 높은 선반 D4
# 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑
# 만들 수 있는 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것을 출력


# T = int(input())
# for t in range(T):
    
#     N, B = map(int, input().split())
#     List = list(map(int, input().split()))
#     List.sort()

#     # 이분탐색으로 B 이하 가장 높은값 찾기
#     small = 0
#     big = N

#     Result = None
#     while small < big:
#         mid = (small + big)//2
#         if List[mid] <= B:
#             Result = List[mid]
#             small = mid + 1
#         else:
#             big = mid


#     print(Result)
    
    
# 장훈이의 높은 선반 D4
# 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑
# 만들 수 있는 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것을 출력

T = int(input())

def dfs(i, s):
    global best

    if s >= best:
        return
    if s >= B:
        best = min(best, s)
        return
    if i == N:
        return

    dfs(i + 1, s + heights[i])
    dfs(i + 1, s)

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort(reverse=True)   # 가지치기 도움됨(선택)

    best = float('inf')
    dfs(0, 0)
    print(f"#{tc} {best - B}")
