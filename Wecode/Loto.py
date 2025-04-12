a = []
for i in range(3):
    r = list(map(int, input().split()))
    a.append(r)

n = int(input())
used = []

for i in range(n):
    used.append(int(input()))

vis = [[False] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        if a[i][j] in used:
            vis[i][j] = True;
            
ok = False;
if (vis[0][0] == True and vis[0][1] == True and vis[0][2] == True):
    ok = True
if (vis[1][0] == True and vis[1][1] == True and vis[1][2] == True):
    ok = True
if (vis[2][0] == True and vis[2][1] == True and vis[2][2] == True):
    ok = True
if (vis[0][0] == True and vis[1][0] == True and vis[2][0] == True):
    ok = True
if (vis[0][1] == True and vis[1][1] == True and vis[2][1] == True):
    ok = True
if (vis[0][2] == True and vis[1][2] == True and vis[2][2] == True):
    ok = True
if (vis[0][0] == True and vis[1][1] == True and vis[2][2] == True):
    ok = True
if (vis[0][2] == True and vis[1][1] == True and vis[2][0] == True):
    ok = True
if (ok):
    print("Yes")
else:
    print("No")
            