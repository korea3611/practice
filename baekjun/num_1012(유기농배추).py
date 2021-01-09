# ###런타임에러###
# import sys
# sys.setrecursionlimit(10000)
#
# def dfs(x,y):
#     visited[x][y] = True
#     directions = [(-1,0),(1,0),(0.-1),(0.1)]
#     for dx, dy in directions:
#         nx, ny = x+dx, y+dy
#         if nx < 0 or nx >= n or ny < 0 or ny >= m:
#             continue
#         if array[nx][ny] and not visited[nx][ny]:
#             dfs(nx,ny)
#
# for _ in range(int(input())):
#     m,n,k = map(int,input().split())
#     array = [[0] * m for _ in range(n)]
#     visited = [[False]*m for _ in range(n)]
#     for _ in range(k):
#         y,x = map(int,input().split())
#         array[x][y] = 1
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             if array[i][j] and not visited[i][j]:
#                 dfs(i,j)
#                 result += 1
#     print(result)

##############두번째코드 정답코드!

import sys
sys.setrecursionlimit(10000)

T = int(input())
b,ck = [],[]
dx, dy = [1,0,-1,0],[0,1,0,-1]

def dfs(x,y):
    global b,ck
    if ck[x][y] == 1:
        return
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if b[xx][yy] == 0 or ck[xx][yy] == 1:
            continue
        dfs(xx, yy)

def process():
    global b,ck
    m,n,k = map(int,input().split())
    b = [[0 for i in range(52)] for _ in range(52)]
    ck = [[0 for i in range(52)] for _ in range(52)]
    for _ in range(k):
        x,y = map(int,input().split())
        b[y+1][x+1] = 1
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if b[i][j] == 0 or ck[i][j] == 1:
                continue
            dfs(i,j)
            ans += 1
    print(ans)

for _ in range(T):
    process()

