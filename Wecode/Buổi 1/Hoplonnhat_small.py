x, y = map(int, input().split())

ans = 0

for h in range(1, min(x, y) // 2 + 1):
    ans = max(ans, (x - 2 * h) * (y - 2 * h) * h)
print(ans)