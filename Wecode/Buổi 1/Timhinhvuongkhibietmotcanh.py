a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab = (b[0] - a[0], b[1] - a[1])

v1 = (-ab[1], ab[0])  
v2 = (ab[1], -ab[0])  

c1 = (a[0] + v1[0], a[1] + v1[1])
d1 = (b[0] + v1[0], b[1] + v1[1])

c2 = (a[0] + v2[0], a[1] + v2[1])
d2 = (b[0] + v2[0], b[1] + v2[1])

v1 = [a, c1, d1, b]
v2 = [a, b, d2, c2]

for v in (v1, v2):
    print(" ".join([f"({x}, {y})" for x, y in v]))
