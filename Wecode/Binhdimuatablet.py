import math

n = int(input())
count = 0
for a in range(1, n):
    b2 = n * n - a * a
    if (a * a > b2):
        break
    b = math.isqrt(b2)
    if b * b == b2 and b > 0:
        count += 1
print(count)