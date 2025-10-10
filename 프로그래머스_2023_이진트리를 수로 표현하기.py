# 프로그래머스_2023_이진트리를 수로 표현하기

# [핵심 요약]
# 10진수를 2진수로 바꾼 뒤,
# 왼쪽에 0을 채워서 (2^n - 1) 길이의 포화 이진 트리로 만들 수 있고,
# 그 트리에서 부모가 0인데 자식이 1인 경우가 없다면,
# ‘표현 가능한 이진 트리’로 인정한다.

def solution(numbers):
    def dfs(tree):
        
        # 포화 이진 트리 형태 문자열을 재귀적으로 검사
        mid = len(tree) // 2
        root = tree[mid]

        # 리프 노드면 항상 가능
        if len(tree) == 1:
            return True
        
        left = tree[:mid]
        right = tree[mid + 1:]
        
        # 부모가 0인데 자식에 1이 있으면 안됨
        if root == '0' and ('1' in left + right):
            return False
        
        return dfs(left) and dfs(right)
    
    answer = []
    
    for num in numbers:
        # 10진수를 2진수로 변환
        b = bin(num)[2:]
        
        # 포화 이진트리 맞추기 (왼쪽에 0 패딩)
        h = 1
        while (1 << h) - 1 < len(b):
            h += 1
        tree = b.zfill((1 << h) - 1)
        
        # 이진 트리 검사
        if dfs(tree):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
