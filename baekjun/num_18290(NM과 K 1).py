n,m,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
c = [[False]*m for _ in range(n)]
ans = -2147483647
dx, dy = [0,0,1,-1],[1,-1,0,0]

def go(px, py, cnt, s):
    if cnt == k:
        global ans
        if ans < s:
            ans = s
        return
    for x in range(px, n):
        for y in range(py if x == px else 0, m):
            if c[x][y]:
                continue
            ok = True
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if c[nx][ny]:
                        ok = False

            if ok:
                c[x][y] = True
                go(x,y, cnt+1, s+a[x][y])
                c[x][y] = False

go(0,0,0,0)
print(ans)
###########################################
n,m,k = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
ck = [[False]*m for _ in range(n)]
ans = -987654321

def go(x, y, cnt, sum):
    global ans
    if cnt == k:
        ans = max(ans, sum)
        return
    if x == n-1 and y == m:
        return

    nx = 0
    ny = 0
    if y == m-1:
        if x == n-1:
            nx = n-1
            ny = m
        else:
            nx = x + 1
            ny = 0
    else:
        nx = x
        ny = y + 1

    bo = True
    if x > 0:
        if ck[x-1][y] == True:
            bo = False
    if y > 0:
        if ck[x][y-1] == True:
            bo = False
    if bo:
        ck[x][y] = True
        go(nx, ny, cnt+1, sum + data[x][y])
        ck[x][y] = False
    go(nx, ny, cnt, sum)

go(0,0,0,0)
print(ans)
