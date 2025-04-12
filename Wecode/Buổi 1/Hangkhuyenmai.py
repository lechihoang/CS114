p = list(map(float, input().split()))
n = len(p)
s1 = sum(p)
s2 = 0
for i in range(n):
    s = input().strip()
    if "%" in s:
        t = s.split('%')[0].split()
        if len(t) > 0:
            token = t[-1]
            if token.lstrip("-").replace(".", "", 1).isdigit():
                add = float(token)
            else:
                s2 += p[i]
                continue
        else:
            s2 += p[i]
            continue
        if "lower than in-store" in s:
            s2 += p[i] / (1 - add / 100)
        elif "higher than in-store" in s:
            s2 += p[i] / (1 + add / 100)
    else:
        s2 += p[i]
have = float(input())
val = min(s1, s2)
if have >= val:
    print("true")
else:
    print("false")