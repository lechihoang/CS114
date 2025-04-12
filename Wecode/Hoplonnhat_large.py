import math

x, y = map(int, input().split())

h_max = int(min((x - 1) // 2, (y - 1) // 2))

n = int(((x + y) - math.sqrt((x + y) ** 2 - 3 * x * y)) / 6)
    
val = []
if h_max >= 1:
    val.append(h_max)
for d in range(0, 2):
    cur = n + d
    if 1 <= cur <= h_max:
        val.append(cur)
    
mx = 0
for h in val:
    cur = h * (x - 2 * h) * (y - 2 * h)
    mx = max(mx, cur)
    
print(mx)