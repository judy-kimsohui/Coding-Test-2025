# 2292_벌집

N = int(input())

count = 1    # 층 수 (결과)
end = 1      # 현재 층의 마지막 번호

while N > end:
    end += 6 * count
    count += 1

print(count)
