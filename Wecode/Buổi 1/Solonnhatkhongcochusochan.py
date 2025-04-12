u = int(input())
if u % 2 == 1: 
    u = u - 2
s = list(str(u))
n = len(s)

f = False

for i in range(n):
    d = int(s[i])
    if d % 2 == 0:
        f = True  
        if d > 0:
            s[i] = str(d - 1)
        else:
            j = i - 1
            while j >= 0:
                prev = int(s[j])
                prev = prev - 1
                while prev >= 1 and prev % 2 == 0:
                    prev = prev - 1
                if prev >= 1:
                    s[j] = str(prev)
                    break
                else:
                    s[j] = '9'
                    j -= 1
            if j < 0:
                s[0] = '0'
            s[i] = '9'
        for k in range(i + 1, n):
                s[k] = '9'

ans = int("".join(s))

print(ans)