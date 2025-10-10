# 2022_사다리
import math

x, y, c = map(float, input().split())

left, right = 0, min(x, y)
result = 0

while right - left > 1e-6:  # 오차 허용
    mid = (left + right) / 2  # 벽 사이 거리 d 후보

    h1 = math.sqrt(x**2 - mid**2)
    h2 = math.sqrt(y**2 - mid**2)
    c_cal = (h1 * h2) / (h1 + h2)

    if c_cal >= c:
        result = mid
        left = mid
    else:
        right = mid

print(f"{result:.3f}")
