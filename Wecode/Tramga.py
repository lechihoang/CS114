a = []
for i in range(2):
    b = input().strip()
    a.append(b)
ok = True;
cnt = 0;
for i in range(2):
    for j in range (2):
        if (a[i][j] == '#'): 
            cnt = cnt + 1
if (cnt == 2):
    if (a[0][0] == '#' and a[1][1] == '#'):
        ok = False
    if (a[0][1] == '#' and a[1][0] == '#'):
        ok = False
if (ok):
    print("Yes")
else:
    print("No");