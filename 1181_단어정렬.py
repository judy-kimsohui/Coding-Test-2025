# 1181_단어정렬

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 중복된 단어는 하나만 남기고 제거

N = int(input())
WordL = []
WordS = set()
for _ in range(N):
    word = input()
    L = len(word)
    if word not in WordS:
        WordS.add(word)
        WordL.append((L, word))
    

WordL = sorted(WordL, key=lambda x:(x[0], x[1]))
for i, word in WordL:
    print(word)