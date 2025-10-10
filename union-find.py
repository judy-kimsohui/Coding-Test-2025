# Union-Find (Disjoint Set Union, DSU) 자료구조 구현


# 초기화: 각 원소가 자기 자신을 부모로 가짐
parent = {x: x for x in ['A', 'B', 'C', 'D', 'E']}

# x가 속한 그룹의 대표를 찾는 함수
def find(x):
    if parent[x] != x:
        # 대표를 바로 연결시켜서 트리 깊이를 줄이는 것
        # A → B → C → D
        parent[x] = find(parent[x])  # 경로 압축 (Path Compression)
    return parent[x]

    # find(D)
    # A ← B
    # A ← C
    # A ← D

# 두 원소가 속한 그룹을 합치는 함수
def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa  # pb의 대표를 pa로 설정
