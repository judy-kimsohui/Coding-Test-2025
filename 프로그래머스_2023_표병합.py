# 프로그래머스_2023_표병합

def solution(commands):
    answer = []
    
    # 50x50 표 초기화
    Excel = [["E"] * 50 for _ in range(50)]
    Merge = [[(-1, -1) for _ in range(50)] for _ in range(50)]
    
    def find_root(r, c):
        """해당 셀의 병합 대표좌표(root)를 찾아 반환"""
        (a, b) = Merge[r][c]
        if (a, b) == (-1, -1):
            return (r, c)
        else:
            return (a, b)

    def get_group(root):
        """루트(root)와 연결된 모든 셀 좌표 반환"""
        group = []
        for i in range(50):
            for j in range(50):
                if find_root(i, j) == root:
                    group.append((i, j))
        return group

    for comd in commands:
        parts = comd.split()
        cmd = parts[0]

        # ✅ UPDATE r c value
        if cmd == "UPDATE" and len(parts) == 4:
            r, c, value = int(parts[1]) - 1, int(parts[2]) - 1, parts[3]
            root = find_root(r, c)
            Excel[root[0]][root[1]] = value

        # ✅ UPDATE value1 value2
        elif cmd == "UPDATE" and len(parts) == 3:
            v1, v2 = parts[1], parts[2]
            for i in range(50):
                for j in range(50):
                    root = find_root(i, j)
                    if Excel[root[0]][root[1]] == v1:
                        Excel[root[0]][root[1]] = v2

        # ✅ MERGE r1 c1 r2 c2
        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(lambda x: int(x) - 1, parts[1:])
            root1 = find_root(r1, c1)
            root2 = find_root(r2, c2)

            if root1 == root2:
                continue  # 이미 같은 그룹

            # 값 있는 쪽으로 병합
            v1, v2 = Excel[root1[0]][root1[1]], Excel[root2[0]][root2[1]]
            if v1 == "E" and v2 != "E":
                Excel[root1[0]][root1[1]] = v2
            # root2를 root1 그룹에 연결
            for i in range(50):
                for j in range(50):
                    if find_root(i, j) == root2:
                        Merge[i][j] = root1
            Merge[root2[0]][root2[1]] = root1

        # ✅ UNMERGE r c
        elif cmd == "UNMERGE":
            r, c = int(parts[1]) - 1, int(parts[2]) - 1
            root = find_root(r, c)
            value = Excel[root[0]][root[1]]

            # 해당 그룹의 모든 셀 해제
            for i, j in get_group(root):
                Merge[i][j] = (-1, -1)
                Excel[i][j] = "E"

            # 원래 셀의 값 복구
            Excel[r][c] = value

        # ✅ PRINT r c
        elif cmd == "PRINT":
            r, c = int(parts[1]) - 1, int(parts[2]) - 1
            root = find_root(r, c)
            val = Excel[root[0]][root[1]]
            answer.append("EMPTY" if val == "E" else val)
    
    return answer
